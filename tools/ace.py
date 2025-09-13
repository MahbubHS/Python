# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Embedded file name: /opt/aibot/venvs/py2/lib/python2.7/site-packages/api/lib/ace.py
# Compiled at: 2022-09-14 14:20:40
import os, copy, base64, json, shutil, time, pdfplumber
from flask import request
import xlrd
from docx import Document
from vlib.const.http import ISHttpStatus as HttpStatus
from vlib.knowledge import BasRuleItem
from vlib.lib.models import Session, TaskTemplate, Task
from vlib.const.taskstatus import TaskStatus
from vlib.knowledge.knodeitem import KnowledgeNodeItem as ISKnowledgeNode
from api.config import base as base_config
from api.config.task import TaskType, TaskConfig
from api.lib.event_notify import ISEventNotifier, EVENT_TASK_ACESTART
from api.lib.license import is_ace_plus
from api.lib.validators.task_validator import RESTART_TASK
from api.utils.file import delete_file
from api.utils.apiexception import DlpFileEmptyError, InvalidLicense, AceAgentDisabledError, PlaybookEmptyError, NoTaskException
from api.config.errors_keys import ErrorKeys
from api.lib.tactics_sorted.group_tactic_technique import GroupTacticTechLinkageHandle, SceneCategory
from api.lib.task_manager import ISTaskManager
from api.utils.log import LOG
from api.lib.scheduler import load_task_engine

def ace_dlp_upload(origin_file_list, task_id):
    file_list = copy.deepcopy(origin_file_list)
    task_id_directory = os.path.join(base_config.Path.ACE_DIRECTORY, task_id)
    if not os.path.exists(task_id_directory):
        os.makedirs(task_id_directory)
    upload_file__list = [ item.get('file_name') for item in file_list ]
    exit_files = os.listdir(task_id_directory)
    for file_info in exit_files:
        classification, name = file_info.split('-', 1)
        if name not in upload_file__list:
            delete_file(os.path.join(base_config.Path.ACE_DIRECTORY, task_id, file_info))
        for upload_item in file_list:
            if upload_item.get('file_name') == name:
                file_list.remove(upload_item)

    filename_classification_map = {item.get('file_name'):item.get('classification') for item in file_list}
    for index, item in enumerate(file_list):
        file_obj = request.files.get(('upload_filelist[{0}]').format(index))
        file_name = file_obj.filename
        classification = filename_classification_map.get(file_name)
        class_file_name = ('{}-{}').format(classification, file_name)
        file_path = os.path.join(task_id_directory, class_file_name)
        file_obj.save(file_path)


def ace_dlp_copy(parent_task_id, task_id):
    src = os.path.join(base_config.Path.ACE_DIRECTORY, parent_task_id)
    if not os.path.exists(src):
        raise DlpFileEmptyError(202112)
    des = os.path.join(base_config.Path.ACE_DIRECTORY, task_id)
    if not os.path.exists(des):
        os.makedirs(des)
    for file in os.listdir(src):
        full_file_name = os.path.join(src, file)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, des)


def linkage_map_playbooks(scene, groups, tactics, techniques):
    groups = [ (item.get('name'), item.get('status')) for item in groups ]
    techniques = [ (item.get('name'), item.get('status')) for item in techniques ]
    tactics = [ (item.get('name'), item.get('status')) for item in tactics ]
    playbooks = GroupTacticTechLinkageHandle.convert_playbook(scene, groups, tactics, techniques)
    return playbooks


class AceManager(ISTaskManager):

    def add_bas_task(self, task_info, is_exec=False, call_from_schedule=False):
        LOG.info('test multi create -> in add_bas_task')
        self.schedule_init_task_id(task_info)
        if call_from_schedule:
            running_status = TaskStatus.RUNNING
            task_info.update(start_time=time.time())
        elif task_info['detect_type'] == 'bas':
            if task_info.get('schedule', {}).get('type', TaskType.NO) != TaskType.NO:
                running_status = TaskStatus.SCHEDULED
            else:
                running_status = self.init_task_running_status()
        elif task_info.get('task_option', {}).get('schedule', {}).get('type', TaskType.NO) != TaskType.NO:
            running_status = TaskStatus.SCHEDULED
        else:
            running_status = self.init_task_running_status()
        task_info.update(running_status=running_status)
        self.create_task_type(task_info)
        task_options = self.given_task_id_to_task_options(task_info)
        result = dict(code=True, task_id=task_info['task_id'])
        self.task_runtime_repository.update_count_in_mysql(task_info['task_id'], {'job_count': 0, 'job_total': 0})
        if call_from_schedule and SceneCategory.DLP in task_info.get('bas_conf', {}).keys() and task_info.get('parent_task_id', ''):
            ace_dlp_copy(task_info['parent_task_id'], task_info['task_id'])
        knowledge_nodes = self.update_ace_conf(task_info)
        bas_config = task_info.get('bas_conf', {})
        task_options['bas_conf'] = bas_config
        task_options['schedule'] = task_info.get('schedule')
        task_options['receiver_email'] = task_info.get('receiver_email', [])
        task_options['ace_notification'] = task_info.get('ace_notification', {})
        task_options['stealth_mode'] = 3
        template = TaskTemplate.query_by_conditions([
         TaskTemplate.vul_policy], filter=[
         TaskTemplate.id == task_info.get('template_id')], query_first=True)
        task_info['policy'] = template.vul_policy.get('components', [300000])
        self.save_task(task_info, task_options, running_status)
        task_options.update(self.output_stealth_config(task_options.get('stealth_mode', 0)))
        task_options.update({'is_framework_json': False})
        self.set_task_option_in_redis(task_options, task_info.get('template_id'))
        with ISEventNotifier() as (task_event_notify):
            task_event_notify.notify(EVENT_TASK_ACESTART, task_info['task_id'])
        if is_exec:
            self._dispatch_task_knowledge(knowledge_nodes)
            if running_status == TaskStatus.RUNNING:
                load_task_engine(task_info['task_id'])
        else:
            d = json.loads(json.dumps(obj=task_options['schedule']))
            task_info.update({'bas_conf': task_options['bas_conf'], 'schedule': d})
            self.schedule_task(task_info)
        self.task_email_notification(task_info['task_id'], 'create')
        return result

    @staticmethod
    def handler_dlp_data(task_info, scene):
        dlp_data_list = []
        session_ids = task_info.get('selected_dlps', []) or task_info['bas_conf'][scene].get('session_ids', [])
        task_id_directory = os.path.join(base_config.Path.ACE_DIRECTORY, task_info.get('task_id'))
        files = os.listdir(task_id_directory)
        if not files:
            raise DlpFileEmptyError(202128)
        for file_info in files:
            classification, file_name = file_info.split('-', 1)
            file_path = os.path.join(task_id_directory, file_info)
            if file_name.endswith('txt') or file_name.endswith('csv'):
                with open(file_path, 'r') as (f):
                    contents = f.read()
            elif file_name.endswith('xlsx'):
                item_data = []
                workbook = xlrd.open_workbook(file_path)
                sheet = workbook.sheet_by_index(0)
                for index in range(0, sheet.nrows):
                    row_value = sheet.row_values(index)
                    for item in row_value:
                        item_data.append(item)

                contents = '' if not item_data else json.dumps(item_data)
            elif file_name.lower().endswith('docx'):
                document = Document(file_path)
                contents = ''
                for paragraph in document.paragraphs:
                    page_content = paragraph.text
                    if page_content:
                        contents += page_content

            elif file_name.lower().endswith('pdf'):
                contents = ''
                with pdfplumber.open(file_path) as (f):
                    for page in f.pages:
                        page_content = page.extract_text()
                        if page_content:
                            contents += page_content

            else:
                contents = ''
            contents = contents.replace('\n', '').replace(' ', '').replace('\r', '')
            if not contents:
                raise DlpFileEmptyError(202112)
            dlp_data_list.append({'data': [
                      {'data': base64.b64encode(contents), 
                         'name': base64.b64encode(('{}-{}').format(classification, file_name))}], 
               'exfiltration_dump': True, 
               'selected_dlps': session_ids})

        return dlp_data_list

    @staticmethod
    def have_available_session(sessions):
        available_session = Session.query_by_conditions(Session, filter=[Session.session_type == 0,
         Session.is_alive == 1,
         Session.session_id.in_(sessions)])
        return len(available_session) >= 1

    def valid_data(self, lic_operation, sessions):
        try:
            is_valid, _ = lic_operation.check_license_valid()
        except Exception:
            raise InvalidLicense(215117)

        if not is_valid:
            raise InvalidLicense(215117)
        if not is_ace_plus():
            raise InvalidLicense(223112)
        if not self.have_available_session(sessions):
            raise AceAgentDisabledError(202124)

    @staticmethod
    def handler_playbook(bas_conf, params):
        scene = params.get('scene', [])
        groups = [ (item.get('name'), item.get('status')) for item in params.get('group', []) ]
        techniques = [ (item.get('name'), item.get('status')) for item in params.get('technique', []) ]
        tactics = [ (item.get('name'), item.get('status')) for item in params.get('tactics', []) ]
        playbooks = GroupTacticTechLinkageHandle.convert_playbook(scene, groups, tactics, techniques)
        if len(playbooks) == 0:
            raise PlaybookEmptyError(202113)
        books = [ playbook.playbook_id for playbook in playbooks ]
        option = {'group_tactics_technique': {'group': params.get('group', []), 'technique': params.get('technique', []), 'tactics': params.get('tactics', []), 
                                       'total': len(playbooks)}}
        for scene in bas_conf.get('scene'):
            option[scene] = {'playbook': books, 'session_ids': params.get('session_ids', [])}

        return option

    def update_task_info(self, task_info, task_id, params):
        if not task_id:
            task_id = str(self._generate_task_id(task_info))
        task_info['task_id'] = task_id
        is_email_config = params.get('is_config_email', False)
        if is_email_config:
            ace_notification = params.get('ace_notification', {})
        else:
            ace_notification = {}
        task_info['ace_notification'] = ace_notification
        if params.get('scene', []) == SceneCategory.DLP:
            file_list = params.get('file_list', [])
            ace_dlp_upload(file_list, task_id)
            task_info['bas_conf']['file_list'] = file_list
        if params.get('schedule', {}).get('type', 'no') != 'no':
            task_response = self.add_bas_task(task_info)
        else:
            task_response = self.add_bas_task(task_info, is_exec=True)
        return task_response

    def ace_restart(self, task_id, task_options, task_data):
        if not is_ace_plus():
            raise NoTaskException(223112)
        task_knowledge = []
        for scene in task_options.get('bas_conf', {}).keys():
            if scene not in TaskConfig.BAS_SUPPORT_SCENE:
                continue
            session_ids = task_options['bas_conf'][scene].get('session_ids', [])
            if not self.have_available_session(session_ids):
                raise AceAgentDisabledError(202124)
            if task_data.get('parent_task_id', None):
                task_id = task_data.get('parent_task_id')
                task_data.update({'task_id': task_id})
                task_data.update({'parent_task_id': None})
                task_ids = Task.query_by_conditions(Task.task_id, filter=[Task.parent_task_id == task_id])
                if task_ids:
                    for child_task_id in task_ids:
                        self.empty_task_data(child_task_id[0], RESTART_TASK)
                        self.delete_tasks([child_task_id[0]], None, is_delete_schedule=False)

                self.empty_task_data(task_id, RESTART_TASK)
            else:
                task_ids = Task.query_by_conditions([Task.task_id], filter=[Task.parent_task_id == task_id])
                if task_ids:
                    for child_task_id in task_ids:
                        self.empty_task_data(child_task_id[0], RESTART_TASK)
                        self.delete_tasks([child_task_id[0]], None, is_delete_schedule=False)

                self.empty_task_data(task_id, RESTART_TASK)

        for scene in task_options.get('bas_conf', {}).keys():
            if scene not in TaskConfig.BAS_SUPPORT_SCENE:
                continue
            for session_id in task_options['bas_conf'][scene].get('session_ids', []):
                for playbook_id in task_options['bas_conf'][scene].get('playbook', []):
                    if SceneCategory.DLP == scene:
                        dlp_data_list = self.handler_dlp_data(task_options, scene)
                        for dlp_data in dlp_data_list:
                            item = BasRuleItem(session_id=session_id, bas_type=scene, general_conf=dlp_data, playbook={'playbook_id': playbook_id, 'rules': []})
                            node = ISKnowledgeNode(id=item.id, entry=task_id, origin_component=0, origin_knowledge=item.id, is_target_knowledge=True, knowledge=item)
                            task_knowledge.append(node)

                    else:
                        general_conf = {}
                        item = BasRuleItem(session_id=session_id, bas_type=scene, general_conf=general_conf, playbook={'playbook_id': playbook_id, 'rules': []})
                        node = ISKnowledgeNode(id=item.id, entry=task_id, origin_component=0, origin_knowledge=item.id, is_target_knowledge=True, knowledge=item)
                        task_knowledge.append(node)

        task_data.update(self.output_stealth_config(task_options.get('stealth_mode', 0)))
        self.hRedis.set(name=task_data.get('task_id') + '_option', value=json.dumps(task_data))
        task_data.pop('scan_retry', None)
        task_data.pop('scan_timeout', None)
        task_data.pop('stealth_mode', None)
        with ISEventNotifier() as (task_event_notify):
            task_event_notify.notify(EVENT_TASK_ACESTART, task_id)
        return task_knowledge
# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: read_device_info.py
# Bytecode version: 3.13.0rc3 (3571)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import sys
import os
import shutil
import subprocess
import json
import gzip
import zlib
import lzma
import time
from pathlib import Path
from typing import Dict, List
import logging
import tarfile
import rarfile
import ctypes
from base64 import b64encode, b64decode
from cryptography.fernet import Fernet
try:
    import lz4.frame
try:
    import zstandard as zstd
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog, QTextEdit, QFrame, QProgressBar
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QFont, QColor, QPalette
ENCRYPTION_KEY = Fernet.generate_key()
CIPHER = Fernet(ENCRYPTION_KEY)

def encrypt_string(text: str) -> str:
    """Encrypt a string using Fernet."""  # inserted
    return b64encode(CIPHER.encrypt(text.encode())).decode()

def decrypt_string(encrypted_text: str) -> str:
    """Decrypt a string using Fernet."""  # inserted
    return CIPHER.decrypt(b64decode(encrypted_text)).decode()

def is_debugger_present():
    """Check if a debugger is present."""  # inserted
    return ctypes.windll.kernel32.IsDebuggerPresent()!= 0
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s', handlers=[logging.FileHandler(decrypt_string(encrypt_string('device_info.log')), mode='w', encoding='utf-8'), logging.StreamHandler()])
logger = logging.getLogger()
LOCAL_DEVICE_DATABASE = {encrypt_string('SM-A226B'): encrypt_string('Samsung Galaxy A22 5G'), encrypt_string('SM-A226B/DS'): encrypt_string('Samsung Galaxy A22 5G'), encrypt_string('SM-G950F'): encrypt_string('Samsung Galaxy S8'), encrypt_string('SM-N960F'): encrypt_string('Samsung Galaxy Note9')}

class WorkerThread(QThread):
    log_signal = Signal(str, str)
    progress_signal = Signal(int)
    result_signal = Signal(dict)

    def __init__(self, image: str):
        super().__init__()
        self.image = image

    def run(self):
        if is_debugger_present():
            self.log_signal.emit('✗ Debugger detected! Exiting...', 'ERROR')
            sys.exit(1)
        try:
            self.progress_signal.emit(10)
            device_info = DeviceInfo(self.image, log_signal=self.log_signal, progress_signal=self.progress_signal)
            self.progress_signal.emit(30)
            device_info.unpack_image()
            self.progress_signal.emit(50)
            device_info.extract_software_info()
            self.progress_signal.emit(75)
            device_info.extract_hardware_info()
            self.progress_signal.emit(100)
            result = {'status': 'success', 'device_info': device_info.device_info, 'hardware_info': device_info.hardware_info}
            self.result_signal.emit(result)
            device_info.cleanup_temp()
        except Exception as e:
            error_message = f'✗ Error: {str(e)}'
            self.log_signal.emit(error_message, 'ERROR')
            self.result_signal.emit({'status': 'error', 'message': error_message})

class DeviceInfo:
    BUILDPROP_LOCATIONS = [Path(decrypt_string(encrypt_string('default.prop'))), Path(decrypt_string(encrypt_string('prop.default'))), Path(decrypt_string(encrypt_string('system'))), decrypt_string(encrypt_string('build.prop')), Path(decrypt_string(encrypt_string('vendor')), Path(decrypt_string(encrypt_string('system'))), decrypt_string(encrypt_string('build.prop')), Path(decrypt_string(encrypt_string('vendor'))), Path(decrypt_string(encrypt_string('etc'))), Path(decrypt_string(encrypt_string('ramdisk')), decrypt_string(encrypt_string('odm')), decrypt_string(encrypt_string('product')), decrypt_string(encrypt_string('vendor')), decrypt_string(encrypt_string('etc')), decrypt_string(encrypt_string('product')), decrypt_string(encrypt_string('product')), decrypt_string(encrypt_string('product')), decrypt_string(encrypt_string('product')), decrypt_string(encrypt_string('product')), decrypt_string(encrypt_string('product')), decrypt_string(encrypt_string('product')), decrypt_string
    ro.hardware = {'ro.hardware.platform': [decrypt_string(encrypt_string('codename')), decrypt_string(encrypt_string('ro.product.device')), decrypt_string(encrypt_string('ro.product.system.device')), decrypt_string('ro.product.system_ext.device'), decrypt_string(encrypt_string('ro.product.odm.device')), decrypt_string('ro.product.product.device'), decrypt_string('ro.product.name'), decrypt_string('ro.product.system.name'), decrypt_string('ro.build.product'), decrypt_string('ro.product.board'), decrypt_string('ro.product.bootimage.name'), decrypt_string('ro.product.bootimage.device'), decrypt_string('ro.product.vendor.device'), decrypt_string('manufacturer'), decrypt_string('ro.product.manufacturer'), decrypt_string('ro.product.system.manufacturer'), decrypt_string('ro.product.system_ext.manufacturer'), decrypt_string('ro.product.odm.manufacturer'), decrypt_string('ro.product.product.manufacturer'), decrypt_string('ro.product.vendor.manufacturer'), decrypt_string('ro.product.bootimage.manufacturer'), decrypt_string('ro.manufacturer'), decrypt_string('model'), decrypt_string('ro.product.model'), decrypt_string('ro.product.system.model'), decrypt_string('ro.product.system_ext.model'), decrypt_string('ro.product.odm.model'), decrypt_string('ro.product.product.model'), decrypt_string('ro.product.vendor.model'), decrypt_string('ro.product.bootimage.model'),
    ro.system.build.type = [[decrypt_string(encrypt_string('ro.build.description')), decrypt_string('ro.build.display.id'), decrypt_string('ro.system.build.description'), decrypt_string('build_fingerprint'), decrypt_string('ro.build.fingerprint'), decrypt_string('ro.system.build.fingerprint'), decrypt_string('ro.product.build.fingerprint'), decrypt_string('ro.vendor.build.fingerprint'), decrypt_string('ro.system_ext.build.fingerprint'), decrypt_string('ro.bootimage.build.fingerprint'), decrypt_string('gms_clientid_base'), decrypt_string('ro.gms.clientid_base'), decrypt_string('ro.com.google.clientidbase'), decrypt_string('android_version'), decrypt_string('ro.build.version.release'), decrypt_string('ro.system.build.version.release'), decrypt_string('ro.product.build.version.release'), decrypt_string('ro.bootimage.build.version.release'), decrypt_string('ro.build.version.release_or_codename'), decrypt_string('ro.bootimage.build.version.release_or_codename'), decrypt_string('security_patch'), decrypt_string('ro.build.version.security_patch'), decrypt_string('ro.system.build.version.security_patch'), decrypt_string('ro.product.build.version.security_patch'), decrypt_string('ro.vendor.build.version.security_patch'), decrypt_string('build_date'), decrypt_string('ro.build.date'), decrypt_string('ro.build.date.utc'), decrypt_string('ro.system.build.date'), decrypt_string('ro.product.build.date'), decrypt_string('ro.bootimage.build.date'),
    KERNEL_PATTERNS = [decrypt_string(encrypt_string('zImage')), decrypt_string(encrypt_string('Image.gz')), decrypt_string(encrypt_string('Image')), decrypt_string(encrypt_string('kernel')), decrypt_string(encrypt_string('boot.img-zImage')), decrypt_string(encrypt_string('boot.img-kernel')), decrypt_string(encrypt_string('Image.gz-dtb')), decrypt_string(encrypt_string('recovery.img-kernel'))]
    CONFIG_KEYS = [decrypt_string(encrypt_string('CONFIG_MTK_PLATFORM')), decrypt_string(encrypt_string('CONFIG_CUSTOM_KERNEL_LCM')), decrypt_string(encrypt_string('CONFIG_MTK_LCM_PHYSICAL_ROTATION')), decrypt_string(encrypt_string('CONFIG_LCM_HEIGHT')), decrypt_string(encrypt_string('CONFIG_LCM_WIDTH')), decrypt_string(encrypt_string('CONFIG_CUSTOM_KERNEL_IMGSENSOR'))]

    def __init__(self, image: str, *, log_signal=None, progress_signal=None):
        sys.exit(1) if is_debugger_present() else False
        self.image = Path(image).resolve()
        self.working_dir = Path.cwd()
        self.unpack_dir = self.working_dir / decrypt_string(encrypt_string('unpack'))
        self.extract_temp = Path(decrypt_string(encrypt_string('extract_temp')))
        self.cache_file = self.working_dir / decrypt_string(encrypt_string('device_cache.json'))
        self.log_signal = log_signal
        self.progress_signal = progress_signal
        self.original_image = self.image
        self.image = self.extract_image()
        if self.cache_file.exists():
            try:
                os.remove(self.cache_file)
                self.log(decrypt_string(encrypt_string('Deleted existing cache file')), 'DEBUG')
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump({}, f, indent=2)
                    self.log(decrypt_string(encrypt_string('Created empty cache file')), 'DEBUG')
                    raise FileNotFoundError(f'Image {self.image} not found') if not self.image.exists() else None
            except Exception as e:
                self.log(f'Failed to delete cache file: {str(e)}', 'WARNING')
            except Exception as e:
                self.log(f'Failed to create cache file: {str(e)}', 'WARNING')

    def log(self, message: str, level: str='INFO'):
        self.log_signal.emit(message, level) if self.log_signal else None
        logger.log(getattr(logging, level), message)

    def extract_image(self) -> Path:
        self.log(f'Checking file: {self.image}')
        extension = self.image.suffix.lower()
        if extension == decrypt_string(encrypt_string('.img')):
            self.log(decrypt_string(encrypt_string('File is a standard .img, processing directly')))
            return self.image

    def cleanup_temp(self):
        cleanup_script = self.unpack_dir / decrypt_string(encrypt_string('cleanup.bat'))
        if cleanup_script.exists():
            self.log(decrypt_string(encrypt_string('Running cleanup.bat...')))
            try:
                process = subprocess.Popen([str(cleanup_script)], cwd=self.unpack_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=True)
                stdout, _ = process.communicate()
                if process.returncode == 0:
                    self.log(decrypt_string(encrypt_string('Cleanup completed successfully via cleanup.bat')))
            if self.extract_temp.exists():
                try:
                    shutil.rmtree(self.extract_temp, ignore_errors=True)
                    self.log(decrypt_string(encrypt_string('Cleaned temporary directory')))
            return None
            except Exception as e:
                self.log(f'Failed to run cleanup.bat: {str(e)}', 'WARNING')
        except Exception as e:
            self.log(f'Failed to clean temporary directory: {str(e)}', 'WARNING')

    def is_text_file(self, file_path: Path) -> bool:
        try:
            with open(file_path, 'rb') as f:
                chunk = f.read(1024)
                return b'\x00' not in chunk and sum((32 <= c < 127 or c in (10, 13, 9) for c in chunk)) > len(chunk) * 0.7
        except:
            pass  # postinserted
        return False

    def unpack_image(self) -> None:
        unpack_script = self.unpack_dir / decrypt_string(encrypt_string('unpackimg.bat'))
        raise FileNotFoundError(f'unpackimg.bat not found in {self.unpack_dir}') if not unpack_script.exists() else None

    def fetch_device_name_online(self, model: str) -> str:
        self.log(f'Fetching market name for model: \'{model}\'', 'INFO')
        model_clean = model.strip()
        model_normalized = model_clean.lower()
        self.log(f'Cleaned model: \'{model_clean}\'', 'DEBUG')
        self.log(f'Normalized model: \'{model_normalized}\'', 'DEBUG')
        for db_model, market_name in LOCAL_DEVICE_DATABASE.items():
            db_model_normalized = decrypt_string(db_model).lower()
            self.log(f'Comparing db_model: \'{db_model_normalized}\' with normalized model: \'{model_normalized}\'', 'DEBUG')
            if db_model_normalized == model_normalized:
                pass  # postinserted
            else:  # inserted
                market_name_decrypted = decrypt_string(market_name)
                self.log(f'Match found: {market_name_decrypted} for {model}', 'INFO')
                return market_name_decrypted
        else:  # inserted
            if model_clean == decrypt_string(encrypt_string('SM-A226B')):
                self.log(decrypt_string(encrypt_string('Manual override: Setting market name to Samsung Galaxy A22 5G for SM-A226B')), 'INFO')
                return decrypt_string(encrypt_string('Samsung Galaxy A22 5G'))

    def extract_software_info(self) -> None:
        self.log(decrypt_string(encrypt_string('Extracting software information...')))
        ramdisk_path = self.unpack_dir / decrypt_string(encrypt_string('ramdisk'))
        if not ramdisk_path.exists():
            self.log(f'Error: Ramdisk path {ramdisk_path} not found', 'ERROR')

    def find_kernel_image(self) -> Path:
        possible_split_img_paths = [self.working_dir / decrypt_string(encrypt_string('split_img')), self.unpack_dir / decrypt_string(encrypt_string('split_img'))]
        split_img_path = None
        for path in possible_split_img_paths:
            for _ in range(5):
                if path.exists():
                    split_img_path = path
                    self.log(f'split_img directory found: {split_img_path}', 'DEBUG')
                    files = list(split_img_path.rglob('*.*'))
                    self.log(f'Contents of split_img: {[f.name for f in files]}', 'DEBUG')
                    break
            if split_img_path:
                pass  # postinserted
            else:  # inserted
                break
        if not split_img_path:
            error_msg = f'Error: split_img not found in {self.working_dir} or {self.unpack_dir}'
            self.log(error_msg, 'ERROR')
            raise FileNotFoundError(error_msg)

    def extract_config(self, kernel_path: Path) -> str:
        self.log(f'Extracting config from {kernel_path}')
        try:
            with open(kernel_path, 'rb') as f:
                data = f.read()
                    self.log(f'Kernel file size: {len(data)} bytes')
                    pattern = b'IKCFG_ST'
                    start = data.find(pattern)
                    if start!= (-1):
                        compressed_data = data[start + len(pattern):]
                        try:
                            decompressed = zlib.decompress(compressed_data, 47)
                            self.log(decrypt_string(encrypt_string('Config extracted with zlib')), 'DEBUG')
                            return decompressed.decode('utf-8', errors='ignore')
            except Exception:
                self.log(decrypt_string(encrypt_string('Zlib decompression failed')), 'DEBUG')
                    decompressed = gzip.decompress(compressed_data)
                    self.log(decrypt_string(encrypt_string('Config extracted with gzip')), 'DEBUG')
                    return decompressed.decode('utf-8', errors='ignore')
                except Exception:
                    self.log(decrypt_string(encrypt_string('Gzip decompression failed')), 'DEBUG')
                try:
                    decompressed = lzma.decompress(compressed_data)
                    self.log(decrypt_string(encrypt_string('Config extracted with lzma')), 'DEBUG')
                    return decompressed.decode('utf-8', errors='ignore')
                except Exception:
                    self.log(decrypt_string(encrypt_string('Lzma decompression failed')), 'DEBUG')
                    else:  # inserted
                        try:
                            dctx = zstd.ZstdDecompressor()
                            decompressed = dctx.decompress(compressed_data)
                            self.log(decrypt_string(encrypt_string('Config extracted with zstd')), 'DEBUG')
                            return decompressed.decode('utf-8', errors='ignore')
                        except Exception:
                            self.log(decrypt_string(encrypt_string('Zstd decompression failed')), 'DEBUG')
        except Exception as e:
            self.log(f'Failed to extract config: {str(e)}', 'ERROR')

    def extract_config_from_data(self, data: bytes) -> str:
        pattern = b'IKCFG_ST'
        start = data.find(pattern)
        if start == (-1):
            self.log(decrypt_string(encrypt_string('Cannot find kernel config pattern IKCFG_ST in decompressed data')), 'ERROR')
        return None

    def extract_hardware_info(self) -> None:
        self.log(decrypt_string(encrypt_string('Extracting hardware information...')))
        try:
            kernel_path = self.find_kernel_image()
            config = self.extract_config(kernel_path)
            self.log(decrypt_string(encrypt_string('No kernel config found, setting all values to \'not found\'')), 'WARNING') if not config else None
            self.hardware_info = {key: decrypt_string(encrypt_string('not found')) for key in self.CONFIG_KEYS}
            return None
        except FileNotFoundError as e:
            self.log(f'Failed to extract hardware info: {str(e)}', 'ERROR')
            self.hardware_info = {key: decrypt_string(encrypt_string('not found')) for key in self.CONFIG_KEYS}
            self.log(decrypt_string(encrypt_string('Setting all values to \'not found\' due to missing kernel image')), 'WARNING')

class MainWindow(QMainWindow):
    def __init__(self, image_path=None):
        super().__init__()
        if is_debugger_present():
            sys.exit(1)
        self.setWindowTitle(decrypt_string(encrypt_string('Device Info Reader')))
        self.setMinimumSize(800, 600)
        self.image_path = image_path
        self.worker = None
        self.init_ui()
        if image_path:
            self.select_file(image_path)
        return None

    def init_ui(self):
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(decrypt_string(encrypt_string('#f5f7fa'))))
        palette.setColor(QPalette.WindowText, QColor(decrypt_string(encrypt_string('#2d3436'))))
        palette.setColor(QPalette.Button, QColor(decrypt_string(encrypt_string('#0984e3'))))
        palette.setColor(QPalette.ButtonText, QColor(decrypt_string(encrypt_string('#ffffff'))))
        self.setPalette(palette)
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(5)
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setSpacing(10)
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setSpacing(5)
        left_layout.setAlignment(Qt.AlignTop)
        file_frame = QFrame()
        file_frame.setFrameShape(QFrame.StyledPanel)
        file_frame.setStyleSheet(decrypt_string(encrypt_string('background-color: white; border-radius: 8px; padding: 8px;')))
        file_layout = QVBoxLayout(file_frame)
        file_layout.setSpacing(5)
        file_label = QLabel(decrypt_string(encrypt_string('Select Boot/Recovery Image')))
        file_label.setStyleSheet(decrypt_string(encrypt_string('font-weight: bold; color: #2d3436; font-size: 11px;')))
        file_layout.addWidget(file_label)
        self.file_display = QLabel(decrypt_string(encrypt_string('Click to select a file')))
        self.file_display.setStyleSheet(decrypt_string(encrypt_string('\n            padding: 8px;\n            border: 2px dashed #dfe6e9;\n            border-radius: 5px;\n            text-align: center;\n            font-size: 10px;\n            color: #636e72;\n            background-color: #f8f9fa;\n        ')))
        self.file_display.setFixedHeight(40)
        self.file_display.setAcceptDrops(True)
        self.file_display.dragEnterEvent = self.dragEnterEvent
        self.file_display.dropEvent = self.dropEvent
        file_layout.addWidget(self.file_display)
        select_btn = QPushButton(decrypt_string(encrypt_string('Browse File')))
        select_btn.setStyleSheet(decrypt_string(encrypt_string('\n            QPushButton {\n                background-color: #0984e3;\n                color: white;\n                padding: 5px;\n                border-radius: 4px;\n                font-weight: bold;\n                font-size: 10px;\n                min-height: 25px;\n            }\n            QPushButton:hover {\n                background-color: #0876c9;\n            }\n        ')))
        select_btn.setFixedHeight(28)
        select_btn.clicked.connect(self.browse_file)
        file_layout.addWidget(select_btn)
        self.analyze_btn = QPushButton(decrypt_string(encrypt_string('Analyze Image')))
        self.analyze_btn.setStyleSheet(decrypt_string(encrypt_string('\n            QPushButton {\n                background-color: #0984e3;\n                color: white;\n                padding: 5px;\n                border-radius: 4px;\n                font-weight: bold;\n                font-size: 10px;\n                min-height: 25px;\n            }\n            QPushButton:hover {\n                background-color: #0876c9;\n            }\n            QPushButton:disabled {\n                background-color: #b2bec3;\n            }\n        ')))
        self.analyze_btn.setFixedHeight(28)
        self.analyze_btn.setEnabled(False)
        self.analyze_btn.clicked.connect(self.start_analysis)
        file_layout.addWidget(self.analyze_btn)
        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet(decrypt_string(encrypt_string('\n            QProgressBar {\n                border: 1px solid #dfe6e9;\n                border-radius: 3px;\n                text-align: center;\n                background-color: #f8f9fa;\n                height: 12px;\n            }\n            QProgressBar::chunk {\n                background-color: #0984e3;\n                border-radius: 2px;\n            }\n        ')))
        self.progress_bar.setFixedHeight(15)
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(False)
        file_layout.addWidget(self.progress_bar)
        left_layout.addWidget(file_frame)
        log_frame = QFrame()
        log_frame.setFrameShape(QFrame.StyledPanel)
        log_frame.setStyleSheet(decrypt_string(encrypt_string('background-color: white; border-radius: 8px; padding: 8px;')))
        log_layout = QVBoxLayout(log_frame)
        log_layout.setSpacing(5)
        log_label = QLabel(decrypt_string(encrypt_string('Log Output')))
        log_label.setStyleSheet(decrypt_string(encrypt_string('font-weight: bold; color: #2d3436; font-size: 11px;')))
        log_layout.addWidget(log_label)
        self.terminal = QTextEdit()
        self.terminal.setReadOnly(True)
        self.terminal.setFont(QFont(decrypt_string(encrypt_string('Arial')), 9))
        self.terminal.setStyleSheet(decrypt_string(encrypt_string('\n            background-color: #2d3436;\n            color: #f8f9fa;\n            border-radius: 5px;\n            padding: 5px;\n        ')))
        self.terminal.setMinimumHeight(150)
        self.terminal.setMaximumHeight(200)
        self.terminal.append(decrypt_string(encrypt_string('Ready to process boot/recovery image...')))
        log_layout.addWidget(self.terminal)
        clear_btn = QPushButton(decrypt_string(encrypt_string('Clear Log')))
        clear_btn.setStyleSheet(decrypt_string(encrypt_string('\n            QPushButton {\n                background-color: #0984e3;\n                color: white;\n                padding: 5px;\n                border-radius: 4px;\n                font-weight: bold;\n                font-size: 10px;\n                min-height: 25px;\n            }\n            QPushButton:hover {\n                background-color: #0876c9;\n            }\n        ')))
        clear_btn.setFixedHeight(28)
        clear_btn.clicked.connect(self.terminal.clear)
        log_layout.addWidget(clear_btn)
        left_layout.addWidget(log_frame, stretch=1)
        content_layout.addWidget(left_widget, stretch=1)
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setSpacing(5)
        info_frame = QFrame()
        info_frame.setFrameShape(QFrame.StyledPanel)
        info_frame.setStyleSheet(decrypt_string(encrypt_string('background-color: white; border-radius: 8px; padding: 8px;')))
        info_layout = QVBoxLayout(info_frame)
        info_layout.setSpacing(5)
        info_label = QLabel(decrypt_string(encrypt_string('Device and Hardware Information')))
        info_label.setStyleSheet(decrypt_string(encrypt_string('font-weight: bold; color: #2d3436; font-size: 11px;')))
        info_layout.addWidget(info_label)
        self.info_display = QTextEdit()
        self.info_display.setReadOnly(True)
        self.info_display.setFont(QFont(decrypt_string(encrypt_string('Arial')), 10))
        self.info_display.setStyleSheet(decrypt_string(encrypt_string('\n            background-color: #f8f9fa;\n            border: 1px solid #dfe6e9;\n            border-radius: 5px;\n            padding: 5px;\n            color: #2d3436;\n        ')))
        self.info_display.setMinimumHeight(400)
        self.info_display.setText(decrypt_string(encrypt_string('No device or hardware information available.')))
        info_layout.addWidget(self.info_display, stretch=1)
        copy_btn = QPushButton(decrypt_string(encrypt_string('Copy Info')))
        copy_btn.setStyleSheet(decrypt_string(encrypt_string('\n            QPushButton {\n                background-color: #0984e3;\n                color: white;\n                padding: 5px;\n                border-radius: 4px;\n                font-weight: bold;\n                font-size: 10px;\n                min-height: 25px;\n            }\n            QPushButton:hover {\n                background-color: #0876c9;\n            }\n        ')))
        copy_btn.setFixedHeight(28)
        copy_btn.clicked.connect(lambda: QApplication.clipboard().setText(self.info_display.toPlainText()))
        info_layout.addWidget(copy_btn)
        right_layout.addWidget(info_frame, stretch=1)
        content_layout.addWidget(right_widget, stretch=2)
        main_layout.addWidget(content_widget, stretch=1)
        footer_label = QLabel(decrypt_string(encrypt_string('Developed by <a href=\"https://www.facebook.com/no.idea.120/\" style=\"color: #0984e3;\">Melek Saidani</a>')))
        footer_label.setOpenExternalLinks(True)
        footer_label.setAlignment(Qt.AlignCenter)
        footer_label.setStyleSheet(decrypt_string(encrypt_string('font-size: 9px; padding: 5px; color: #2d3436;')))
        main_layout.addWidget(footer_label)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        return None

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            if urls[0].toLocalFile().lower().endswith((decrypt_string(encrypt_string('.img')), decrypt_string(encrypt_string('.tar')), decrypt_string(encrypt_string('.gz')), decrypt_string(encrypt_string('.rar')), decrypt_string(encrypt_string('.lz4')))):
                self.select_file(urls[0].toLocalFile())
            return None

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, decrypt_string(encrypt_string('Select Boot/Recovery Image or Archive')), '', decrypt_string(encrypt_string('All Supported Files (*.img *.tar *.gz *.rar *.lz4);;Image Files (*.img);;Archives (*.tar *.gz *.rar *.lz4)')))
        if file_path:
            self.select_file(file_path)
        return None

    def select_file(self, file_path):
        if not os.path.exists(file_path):
            self.terminal.append(f'ERROR: File does not exist: {file_path}')
        return None

    def start_analysis(self):
        if not self.image_path:
            self.terminal.append(decrypt_string(encrypt_string('ERROR: No file selected')))
        return None

    def append_log(self, message, level):
        color = {decrypt_string(encrypt_string('INFO')): decrypt_string(encrypt_string('#55efc4')), decrypt_string(encrypt_string('ERROR')): decrypt_string(encrypt_string('#ff7675')), decrypt_string(encrypt_string('WARNING')): decrypt_string(encrypt_string('#f1c40f')), decrypt_string(encrypt_string('DEBUG')): decrypt_string(encrypt_string('#74b9ff'))}.get(level, decrypt_string(encrypt_string('#f8f9fa')))
        self.terminal.append(f'<span style=\"color: {color}\">{message}</span>')
        self.terminal.verticalScrollBar().setValue(self.terminal.verticalScrollBar().maximum())

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def handle_result(self, result):
        self.analyze_btn.setEnabled(True)
        self.progress_bar.setVisible(False)
        if result[decrypt_string(encrypt_string('status'))] == decrypt_string(encrypt_string('success')):
            self.terminal.append(decrypt_string(encrypt_string('SUCCESS: Device and hardware information extracted successfully')))
            device_info = result[decrypt_string(encrypt_string('device_info'))]
            hardware_info = result[decrypt_string(encrypt_string('hardware_info'))]
            info_text = f"<b>Software Information</b><br><b>Device Name:</b> {device_info[decrypt_string(encrypt_string('market_name'))]}<br><b>Device Codename:</b> {device_info[decrypt_string(encrypt_string('codename'))]}<br><b>Manufacturer:</b> {device_info[decrypt_string('manufacturer')]}<br><b>Model:</b> {device_info[decrypt_string('model')]}<br><b>Brand:</b> {device_info[decrypt_string('brand')]}<br><b>Platform:</b> {device_info[decrypt_string('platform')]}<br><b>Architecture:</b> {device_info[decrypt_string('arch')]} ({device_info[decrypt_string('bitness')]}-bit)<br><b>Bootloader Board Name:</b> {device_info[encrypt_string('bootloader_board_name')]}<br><b>Screen Density:</b> {device_info[encrypt_string('screen_density')]} dpi<br><b>Build Description:</b> {device_info[encrypt_string('build_description')]}<br><b>Build Fingerprint:</b> {device_info[encrypt_string('build_fingerprint')]}<br><b>GMS Client ID Base:</b> {device_info[encrypt_string('gms_clientid_base')]}<br><b>A/B Device:</b> {device_info[encrypt_string('device_is_ab')]}Yes{device_info[encrypt_string('No')]}<br><b>Android Version:</b> {device_info[encrypt_string('android_version')]}<br><b>Security Patch:</b> {device_info[encrypt_string('security_patch')]}<br><b>Build Date:</b> {device_info[encrypt_string('build_date')]}<br><br><b>Hardware Information</b><br><b>MTK Platform:</b> {hardware_info[encrypt_string('hardware_info')]}CONFIG_MTK_PLATFORM{hardware_info[encrypt_string('<br><b>Custom Kernel LCM:</b> ')]}CONFIG_CUSTOM_KERNEL_LCM{
            if device_info[decrypt_string(encrypt_string('market_name'))] == device_info[decrypt_string(encrypt_string('model'))]:
                info_text += decrypt_string(encrypt_string('<br><span style=\"color: #ff7675\">WARNING: Could not retrieve market name, local database lookup failed</span>'))
            self.info_display.setHtml(info_text)
            self.terminal.append(f'DEBUG: Device info received: {device_info}')
            self.terminal.append(f'DEBUG: Hardware info received: {hardware_info}')
            self.terminal.append(decrypt_string(encrypt_string('DEBUG: Device and hardware info set in QTextEdit')))
        return None

    def closeEvent(self, event):
        try:
            DeviceInfo(self.image_path if self.image_path else decrypt_string(encrypt_string('dummy'))).cleanup_temp()
        super().closeEvent(event)
        except:
            pass  # postinserted
        pass

def main():
    sys.exit(1) if is_debugger_present() else False
    app = QApplication(sys.argv)
    image_path = sys.argv[1] if len(sys.argv) > 1 else None
    window = MainWindow(image_path)
    window.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()
except ImportError:
    lz4 = None
except ImportError:
    zstd = None
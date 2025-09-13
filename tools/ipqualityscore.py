#!/usr/bin/env python3

'''

+-----------------------------------------+
|  PROJECT     : IPQUALITYSCORE USAGE CHK |
|  DESCRIPTION : CHECK API KEY            |
|  RELEASE     : V1                       |
|  AUTHOR      : @F4C3R100                |
+-----------------------------------------+

'''

import requests
import json

def get_response(api_key):
	return requests.get('https://www.ipqualityscore.com/api/json/account/'+api_key).content

def format(__input__):
	try:
		dec = json.loads(__input__.decode('utf-8'))
	except: 
		dec = '__empty__'
		credits = '\033[31mINVALID_API'
	try:
		if dec.get('credits'):
			credits = str(dec.get('credits')) 
		elif dec.get('credits') == None:
			if """You have insufficient credits to make this query""" in dec.get('message'):
				credits = '\033[31mEXPIRED'
			else:
				credits = '\033[31mDEAD'


	except:
		if """You have insufficient credits to make this query""" in dec.get('message'):
			credits = '\033[31mEXPIRED'
	return f"\033[34;1m[\033[37mCREDITS LEFT\033[34m]: \033[33m"+str(credits)+"\033[0m"

api_key = input('\033[37;1mEnter your API Key:\033[33;1m ')

print(format(get_response(api_key)))

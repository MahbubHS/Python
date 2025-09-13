#!/usr/bin/python27
# -*- coding: utf-8 -*-
import sys
import os
import requests, re, sys, threading
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[96m'
purple = '\033[95m'
reset = '\033[0m'



def cls():
    try:
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])
    except:
        pass
cls()

print ("""
 {}
  _ _ _                 _             _   _           _   _             _             {}
 (_) | |               (_)           | | (_)     /\  | | | |           | |            {}
  _| | |_   _ _ __ ___  _ _ __   __ _| |_ _     /  \ | |_| |_ __ _  ___| | _____ _ __ {}
 | | | | | | | '_ ` _ \| | '_ \ / _` | __| |   / /\ \| __| __/ _` |/ __| |/ / _ \ '__|{}
 | | | | |_| | | | | | | | | | | (_| | |_| |  / ____ \ |_| || (_| | (__|   <  __/ |   {}
 |_|_|_|\__,_|_| |_| |_|_|_| |_|\__,_|\__|_| /_/    \_\__|\__\__,_|\___|_|\_\___|_|   {}
{}
""".format(green, green, green, green, red, red, red, reset))


a = 0
total = 0
def main(plugin, kntl):
	result = open(plugin+".txt","a")
	global a
	global total
	while(a < int(kntl)):
		a = a + 1
		print("[+] Scraping Page {}").format(a)
		headers = {"User-agent":"Mozilla 5/0 Linux"}
		try:
			text = requests.get("http://pluginu.com/"+plugin+"/"+str(a), headers=headers, timeout=10).text
			list = re.findall('<p style="margin-bottom: 20px">(.*?)</p></a>', text)
			for i in list:
				total = total + 1
				print("{}[X] {}----> {}"+str(i)).format(green, red, reset)
				result.write(i+'\n')
		except Exception as err:
			print("{}[-] "+str(err)).format(red)
		print("{}[*] Total "+str(total)).format(green)

try:
	plug = sys.argv[1]
	page = sys.argv[2]
except:
	print("python2.7 illuminatiattacker.py [wp plugin] [page]")
	exit()

main(plug,page)


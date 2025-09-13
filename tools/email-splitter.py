#!/usr/bin/python3

# Email Sorter 

import os, time, sys
from termcolor import colored

# Remove # to enable hq domains, make sure you make an # on the domains.

domains = ["hotmail.com", "gmail.com", "yahoo.com", "web.de", "t-online.de", "outlook.com", "protonmail.com","office.com","rackspace.com","icloud.com", "sendgrid.com", "rackspace.com", ""]

#bank_domains = ["bankofamerica.com","barclays.co.uk"]
#domains = ["aol.com","gmail.com","gmail.org","gmail.de","hotmail.com","hotmail.de","hotmail.uk","googlemail.com","gmx.de","bol.com","freenet.de","gmx.com","gmx.ru","hotmail.co.uk","hotmail.nl","icloud.com","protonmail.com","live.com","msn.com","live.fr","live.co.uk","mail.ru","orange.fr","rediffmail.com","rocketmail.com","t-online.de","web.de","yahoo.com","yahoo,de","yandex.com","yandex.ru","yopmail.com"]

os.system('clear||cls;')


print("""
                        _ __          \033[34m            __          \033[0m
  ___  ____ ___  ____ _(_) /     \033[34m_________  _____/ /____  _____\033[0m
 / _ \/ __ `__ \/ __ `/ / /\033[31m_____\033[34m/ ___/ __ \/ ___/ __/ _ \/ ___/\033[0m
/  __/ / / / / / /_/ / / /\033[31m_____\033[34m(__  ) /_/ / /  / /_/  __/ /    \033[0m
\___/_/ /_/ /_/\__,_/_/_/     \033[34m/____/\____/_/   \__/\___/_/     \033[0m
                                                              
	""")

combo = input(colored("[>] COMBO : ", 'green'))

inputs = open(combo, "r", encoding="utf-8").read().splitlines()
for i in inputs:
	try:
		user = i.split(":")[0]
		password = i.split(":")[1]
		t = user.split("@")[1]
	except Exception as e:
		continue
inputs = open(combo, "r").read().splitlines()
try:
	os.system('mkdir maillist')
	try:
		os.system('cd maillist; rm *.txt')
	except Excpetion as e:
		pass
except Exception:
	pass
time.sleep(1.5)

for i in inputs:
	for domain in domains:
		try:
			user = i.split(":")[0]
			password = i.split(":")[1]
			t = user.split("@")[1]
			if domain == t:
				open(f"maillist/{domain}_combo.txt", "a").write(i + "\n")
				open(f"maillist/{domain}_maillist.txt", "a").write(user + "\n")
				print(colored(f"=> Saved hit: ", 'green'), colored(i, 'blue'), colored(f" => maillist/{domain}.txt", 'yellow'))
		except Exception as e:
			continue



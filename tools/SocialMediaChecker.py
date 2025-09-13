import requests

class ChecK():

    def __init__(self):
        self.email = str(input("Enter Email:\033[35m "))
        self.debug = 0
        self.twitter()

    def PrintT(self):
        print((f"\033[32m{self.email} = Linked\033[0m"+"\n"))

    def PrintF(self):
        print((f"\033[31m{self.email} = Unlinked\033[0m"+"\n"))

    def twitter(self):
        print("==================")
        print("\033[34m[\033[37m+\033[34m] \033[33mTwitter \033[34m[\033[37m+\033[34m]")
        print("")
        r = requests.Session()
        url = "https://api.twitter.com/i/users/email_available.json?email="+self.email
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
        Host = "api.twitter.com"
        Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        r.headers = {'User-Agent': user_agent}
        r.headers = {'Host': Host}
        r.headers = {'Accept': Accept}
        req = r.get(url).json()
        text = str(req)
        if self.debug:
            print(text)
            print('')
        if text.find("'valid': False") == True:
            self.PrintT() 
        else:
            self.PrintF()
        self.instagram()

    def instagram(self):
        print("==================")
        print("\033[34m[\033[37m+\033[34m] \033[33mInstagram \033[34m[\033[37m+\033[34m]")
        print("")
        r = requests.Session()
        url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        r.headers = {'user-agent': user_agent}
        r.headers.update({'X-CSRFToken': "missing"})
        data = {"email_or_username":self.email}
        req = r.post(url,data=data)
        if self.debug:
            print((req.text))
            print('')
        if req.text.find("We sent an self.email to")>=0:
            self.PrintT()
        elif req.text.find("password")>=0:
            self.PrintT()
        elif req.text.find("sent")>=0:
            self.PrintT()
        else:
            self.PrintF()
        self.snacphat()

    def snacphat(self): 
        print("==================")
        print("\033[34m[\033[37m+\033[34m] \033[33mSnapchat \033[34m[\033[37m+\033[34m]")
        print("")
        r = requests.Session()
        url = "https://accounts.snapchat.com/accounts/merlin/login"
        r.headers = {'Host': 'accounts.snapchat.com','Accept': 'application/json, text/plain, */*','Accept-Encoding': 'gzip, deflate, br','X-XSRF-TOKEN': 'missing','Content-Type': 'application/json','Origin': 'https://accounts.snapchat.com','User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 'Connection':'keep-alive','Referer': 'https://accounts.snapchat.com/accounts/merlin/login'}
        cookies = {'xsrf_token':'missing'}
        data = {'email':self.email,'app':'BITMOJI_APP'}
        req = r.post(url, cookies=cookies, json=data)
        if self.debug:
            print((req.text)) # If the response is blank, it means Unlinked .
            print('')
        if req.text.find("hasSnapchat") >= 0 :
            self.PrintT()
        else:
            self.PrintF()
        


if __name__ == "__main__":
    print("""

             [-] SocialMediaChecker [-]
          [ Twitter - Instagram - Snapchat ]
\033[31m        ======================================= 
        \033[34m[\033[37m+\033[34m] \033[37mProgramming By : Remax Alghamdi . \033[31m|
        \033[34m[\033[37m+\033[34m] \033[37mInstagram: @OQO .                 \033[31m|
        \033[34m[\033[37m+\033[34m] \033[37mDiscord : Remax#6666 .            \033[31m|
        \033[34m[\033[37m+\033[34m] \033[37mGithub : Fah4d .                  \033[31m|
        =======================================\033[0m

        """)
    ChecK()


print('')    
print('Press enter to exit .')
input('')
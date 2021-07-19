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
3- Sqlmap İle Dbs :ek
4- Waff Bypass Sql
5- Site İp Adresi Öğrenme
_______________________
""")
vur = input("Lütfen yapacağınızı seçiniz -> ")
if vur == "4":
   vur4 = input("Example : https://otuzbir.com/ => ")
   os.system("cd sqlmap +" "python3 sqlmap.py +" "+vur4 +" --dbs --batch)
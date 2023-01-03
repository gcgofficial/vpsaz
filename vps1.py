# coding: utf-8

"""

"""

from os import system
import re, random, sys, time, platform
try:
	from bs4 import BeautifulSoup as par
	from requests import *
except:
	exit("\n\x1b[1;96m[\x1b[1;91m!\x1b[1;96m] MODULE BELUM TERINSTALL SEMUA\n    SILAHKAN BACA README.md\n")

if platform.python_version().split(".")[0] != "3":
	exit("\x1b[1;96m[\x1b[1;91m!\x1b[1;96m] KETIK: python "+sys.argv[0])

def Membuat_ssl(id, cookies, user, pw, server):
	data = {"serverid":id,"username":user,"password":pw}
	agent = open("ua.txt","r").read()
	acak = random.choice(agent.split("\n"))
	head = {"Host":"www.speedssh.com","Connection":"keep-alive","Accept":"*/*","Origin":"https://www.speedssh.com","X-Requested-With":"XMLHttpRequest","User-Agent":acak,"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Referer":server,"Accept-Encoding":"gzip, deflate","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	posd = post("https://www.speedssh.com/create-ssl-30-days.php", headers=head, data=data, cookies={"PHPSESSID":cookies}).text
	if "Your Account has been successfully created !" in posd:
		print("  \x1b[1;91m>>> \x1b[1;96mACCOUNT \x1b[1;92mBERHASIL \x1b[1;96mDIBUAT")
		print("  \x1b[1;91m> \x1b[1;96mUSERNAME \x1b[1;91m:\x1b[1;92m "+re.search("Username\s\s:\s(.*?)<br>", str(posd)).group(1))
		print("  \x1b[1;91m> \x1b[1;96mPASSWORD \x1b[1;91m:\x1b[1;92m "+re.search("Password\s\s:\s(.*?)<br>", str(posd)).group(1))
		print("  \x1b[1;91m> \x1b[1;96mHOST     \x1b[1;91m:\x1b[1;92m "+re.search("Host\sIP\s\s\s:\s(.*?)<br>", str(posd)).group(1))
		print("  \x1b[1;91m> \x1b[1;96mPROTOCOL \x1b[1;91m:\x1b[1;92m SSL/TLS")
		print("  \x1b[1;91m> \x1b[1;96mSSL PORT \x1b[1;91m:\x1b[1;92m 443")
		print("  \x1b[1;91m> \x1b[1;96mOPENSSH PORT  \x1b[1;91m:\x1b[1;92m 22,109,110")
		print("  \x1b[1;91m> \x1b[1;96mDROPBEAR PORT \x1b[1;91m:\x1b[1;92m 444,143,80")
		print("  \x1b[1;91m> \x1b[1;96mCREATE ACCOUNT\x1b[1;91m:\x1b[1;92m "+re.search("on : (.*?)<br>", str(posd)).group(1).replace("-", " ").upper())
		print("  \x1b[1;91m> \x1b[1;96mEXPIRE ACCOUNT\x1b[1;91m:\x1b[1;92m "+re.search("expire on (.*?).<br>", str(posd)).group(1).replace("-", " ").upper()+"\n")
	elif "Username already exists !" in posd:
		exit("  \x1b[1;96m[\x1b[1;91m*\x1b[1;96m] USERNAME SUDAH DIBUAT DENGAN ORANG\n")
	else:
		exit("  \x1b[1;96m[\x1b[1;91m+\x1b[1;96m] KAMU TELAH MEMBUAT AKUN MELEWATI BATAS\n")

def Membuat_ssh(id, cookies, user, pw, server):
	data = {"serverid":id,"username":user,"password":pw}
	agent = open("ua.txt","r").read()
	acak = random.choice(agent.split("\n"))
	head = {"Host":"www.speedssh.com","Connection":"keep-alive","Accept":"*/*","Origin":"https://www.speedssh.com","X-Requested-With":"XMLHttpRequest","User-Agent":acak,"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Referer":server,"Accept-Encoding":"gzip, deflate","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	posd = post("https://www.speedssh.com/create-ssh-30-days.php", headers=head, data=data, cookies={"PHPSESSID":cookies}).text
	if "Your Account has been successfully created !" in posd:
		print("  \x1b[1;91m>>> \x1b[1;96mACCOUNT \x1b[1;92mBERHASIL \x1b[1;96mDIBUAT")
		print("  \x1b[1;91m> \x1b[1;96mUSERNAME \x1b[1;91m:\x1b[1;92m "+re.search("Username\s\s:\s(.*?)<br>", str(posd)).group(1))
		print("  \x1b[1;91m> \x1b[1;96mPASSWORD \x1b[1;91m:\x1b[1;92m "+re.search("Password\s\s:\s(.*?)<br>", str(posd)).group(1))
		print("  \x1b[1;91m> \x1b[1;96mHOST     \x1b[1;91m:\x1b[1;92m "+re.search("Host\sIP\s\s\s:\s(.*?)<br>", str(posd)).group(1))
		print("  \x1b[1;91m> \x1b[1;96mPROTOCOL \x1b[1;91m:\x1b[1;92m TCP AND UDP")
		print("  \x1b[1;91m> \x1b[1;96mSSL PORT \x1b[1;91m:\x1b[1;92m 444")
		print("  \x1b[1;91m> \x1b[1;96mOPENSSH PORT  \x1b[1;91m:\x1b[1;92m 22,109")
		print("  \x1b[1;91m> \x1b[1;96mDROPBEAR PORT \x1b[1;91m:\x1b[1;92m 443,80,143")
		print("  \x1b[1;91m> \x1b[1;96mCREATE ACCOUNT\x1b[1;91m:\x1b[1;92m "+re.search("on : (.*?)<br>", str(posd)).group(1).replace("-", " ").upper())
		print("  \x1b[1;91m> \x1b[1;96mEXPIRE ACCOUNT\x1b[1;91m:\x1b[1;92m "+re.search("expire on (.*?).<br>", str(posd)).group(1).replace("-", " ").upper()+"\n")
	elif "Username already exists !" in posd:
		exit("  \x1b[1;96m[\x1b[1;91m*\x1b[1;96m] USERNAME SUDAH DIBUAT DENGAN ORANG\n")
	else:
		exit("  \x1b[1;96m[\x1b[1;91m+\x1b[1;96m] KAMU TELAH MEMBUAT AKUN MELEWATI BATAS\n")

class SSL_TLS:
	def __init__(self):
		self._nom = 0
		self.link = []

	def Chek(self):
		self.cek = par(get("https://speedssh.com/ssl-server-30-days").text, "html.parser")
		for one in self.cek.find_all("div", attrs={"class":"plan-hp"}):
			for two in one.find_all("h1"):
				self._nom += 1
				print("  \x1b[1;96m{\x1b[1;92m"+str(self._nom)+"\x1b[1;96m}\x1b[1;96m "+two.text)
			for url in one.find_all("a", attrs={"class":"order-plan"}):
				self.link.append(url.get("href"))

		self.pilih = input("\x1b[1;96m☆━━━━━━━━━━━━━━━━ - ━━━━━━━━━━━━━━☆\n  \x1b[1;96m>>> ")
		while self.pilih == "":
			print(" \x1b[1;91m >>>\x1b[1;96m YANG BENER NGENTOD\x1b[1;91m!")
			self.pilih = input("  \x1b[1;96m>>> ")
		try:
			chekin = self.link[int(self.pilih) - 1]
		except (ValueError, IndexError):
			exit("  \x1b[1;96m[\x1b[1;91m!\x1b[1;96m] MASUKAN ANGKANYA AJA BRO..")
		cek_2 = par(get(chekin).text, "html.parser")
		if cek_2.find("div", class_="progress-bar progress-bar-danger") is None:
			serverid = cek_2.find('input', {"type":"hidden"}).get("value")
			cookie = re.search("PHPSESSID=(\w+)\sfor", str(get(chekin).cookies)).group(1)
			print("\x1b[1;91m\x1b[1;96m☆━━━━━━━━━━━━━━━━ - ━━━━━━━━━━━━━━☆")
			user = input("  \x1b[1;95m==> \x1b[1;93mSET USERNAME:\x1b[1;96m ")
			pasw = input("  \x1b[1;95m==> \x1b[1;93mSET PASSWORD: \x1b[1;96m")
			print("\x1b[1;96m☆━━━━━━━━━━━━━━━━ - ━━━━━━━━━━━━━━☆")
			Membuat_ssl(serverid, cookie, user, pasw, chekin)
		if cek_2.find("div", class_="progress-bar progress-bar-danger") is not None:
			exit("  \x1b[1;96m[\x1b[1;91m#\x1b[1;96m] ACCOUNT NOT AVAILABLE\n      SILAHKAN PILIH SERVER LAIN..\n")
			time.sleep(2)
			system('python '+sys.argv[0])
			
			
class SSH:
	def __init__(self):
		self._num = 0
		self.link = []

	def Chek(self):
		self.cek = par(get("https://speedssh.com/ssh-server-30-days").text, "html.parser")
		for one in self.cek.find_all("div", attrs={"class":"plan-hp"}):
			reg = re.findall("<h1>(.*?)</h1>", str(one))
			for judul in reg:
				self._num += 1
				print("  \x1b[1;96m{\x1b[1;92m"+str(self._num)+"\x1b[1;96m}\x1b[1;96m "+judul)
			for url in one.find_all("a", attrs={"class":"order-plan"}):
				self.link.append(url.get("href"))

		self.pilih = input("\x1b[1;96m☆━━━━━━━━━━━━━━━━ - ━━━━━━━━━━━━━━☆\n  \x1b[1;96m>>> ")
		while self.pilih == "":
			print(" \x1b[1;91m >>>\x1b[1;96m YANG BENER NGENTOD\x1b[1;91m!")
			self.pilih = input("  \x1b[1;96m>>> ")
		try:
			chekin = self.link[int(self.pilih) - 1]
		except (ValueError, IndexError):
			exit("  \x1b[1;96m[\x1b[1;91m!\x1b[1;96m] MASUKAN ANGKANYA AJA BRO..")
		cek_2 = par(get(chekin).text, "html.parser")
		if cek_2.find("div", class_="progress-bar progress-bar-danger") is None:
			serverid = cek_2.find('input', {"type":"hidden"}).get("value")
			cookie = re.search("PHPSESSID=(\w+)\sfor", str(get(chekin).cookies)).group(1)
			print("\x1b[1;91m\x1b[1;96m☆━━━━━━━━━━━━━━━━ - ━━━━━━━━━━━━━━☆")
			user = input("  \x1b[1;99m==> \x1b[1;96mSET USERNAME:\x1b[1;96m ")
			pasw = input("  \x1b[1;99m==> \x1b[1;96mSET PASSWORD: \x1b[1;96m")
			print("\x1b[1;91m\x1b[1;96m☆━━━━━━━━━━━━━━━━ - ━━━━━━━━━━━━━━☆")
			Membuat_ssh(serverid, cookie, user, pasw, chekin)
		if cek_2.find("div", class_="progress-bar progress-bar-danger") is not None:
			exit("  \x1b[1;96m[\x1b[1;91m#\x1b[1;96m] ACCOUNT NOT AVAILABLE\n      SILAHKAN PILIH SERVER LAIN..\n")
			time.sleep(2)
			system('python '+sys.argv[0])		
			


def Menu():
        print("""
   \x1b[1;93m  __     ______  ____      
 \ \   / /  _ \/ ___|     
  \ \ / /| |_) \___ \     
   \ V / |  __/ ___) |    
  __\_/ _|_|  _|____/____ 
 |  ___|  _ \| ____| ____|
 | |_  | |_) |  _| |  _|  
 |  _| |  _ <| |___| |___ 
 |_|   |_| \_\_____|_____|
                          
\x1b[1;96m SCRIPT TERMUX SSH BY GCG OFFICIAL
           YT GCG OFFICIAL
           AUTHOR : AZS VPN
\x1b[1;96m☆━━━━━━━━━━━━━━━━ - ━━━━━━━━━━━━━━☆
\x1b[1;92m.           VPS TERMUX FREE
\x1b[1;96m☆━━━━━━━━━━━━━━━━ - ━━━━━━━━━━━━━━☆
\x1b[1;96m  {\x1b[1;92m01\x1b[1;96m} \x1b[1;92m SSH SSL/TLS. \x1b[1;91m           :ONLINE
\x1b[1;96m  {\x1b[1;92m02\x1b[1;96m} \x1b[1;92m SSH 30D TLS/NON TLS   \x1b[1;91m  :ONLINE
\x1b[1;96m  {\x1b[1;92m03\x1b[1;96m} \x1b[1;92m VMESS TLS/NON TLS.  \x1b[1;91m    :ONLINE
\x1b[1;96m  {\x1b[1;92m04\x1b[1;96m} \x1b[1;92m TROJAN TLS/NON TLS.  \x1b[1;91m   :ONLINE
\x1b[1;96m  {\x1b[1;92m05\x1b[1;96m} \x1b[1;92m SSH SLOWDNS         \x1b[1;91m    :ONLINE
\x1b[1;96m  {\x1b[1;92m06\x1b[1;96m} \x1b[1;92m V2RAY TLS/NON TLS .   \x1b[1;91m  :ONLINE
\x1b[1;96m  {\x1b[1;91m00\x1b[1;96m} \x1b[1;92m【KELUAR】
\x1b[1;96m☆━━━━━━━━━━━━━━━━ - ━━━━━━━━━━━━━━☆
\x1b[1;96m☆━━━━━━━━━━━━━━━━ - ━━━━━━━━━━━━━━☆""")
        pilih = input("  \x1b[1;96m>>> \x1b[1;92m")
        while pilih == "":
                print(" \x1b[1;91m >>>\x1b[1;96m YANG BENER NGENTOD\x1b[1;91m!")
                pilih = input("  \x1b[1;96m>>> \x1b[1;92m")
        if pilih in ("1","01"):
                nice = SSL_TLS
        elif pilih in ("2","02"):
                nice = SSH
        elif pilih in ("0","00"):
                exit("\x1b[1;96m☆━━━━━━━━━━━━━━━━ - ━━━━━━━━━━━━━━☆\n \x1b[1;96mJOSSS\n")
        else:
              	exit(" \x1b[1;91m >>> \x1b[1;97mMAAF MENU \x1b[1;91m'\x1b[1;97m"+pilih+"\x1b[1;91m'\x1b[1;97m TIDAK DITEMUKAN\n")
        print("\x1b[1;96m☆━━━━━━━━━━━━━━━━ - ━━━━━━━━━━━━━━☆")
        nice().Chek()                                                                                
if __name__=="__main__":
        system('clear')
        try:
                Menu()
        except Exception as er:
                exit("\n \x1b[1;96m [\x1b[1;91m!\x1b[1;96m] ERROR: "+str(er))
                
                
                
                
                
                
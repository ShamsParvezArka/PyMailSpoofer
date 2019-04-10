#-*-coding: UTF-8 -*-
import os
import time

def disclimer():
	print ""
	print "DISCLIMER: This tool is only for ethical hacking. It doesn't promote any Illigal accivities(!)"
	print ""

def mainpart():
	print "[*] this tool will activate your 'Apache server' and 'web browser'(Firefox) "
	time.sleep(2)
	print ""
	print "[+] activating Apache server ..."
	time.sleep(1)
	os.system("service apache2 start")

	print "[*] creating server directory ..."
	time.sleep(1)
	os.system("rm -r /var/www/html")
	os.system("cp -r html /var/www/")

	print "[!] done"
	time.sleep(0.2)
	print "[!] directory path: /var/www/html/"
	print "[+] activating Firefox ..."
	time.sleep(1)
	print ""

	os.system("firefox 127.0.0.1")

def banner():
	print """
	                              _ _                        __
	                             (_) |                      / _|
	  _ __  _   _ _ __ ___   __ _ _| |___ _ __   ___   ___ | |_ ___ _ __
	 | '_ \| | | | '_ ` _ \ / _` | | / __| '_ \ / _ \ / _ \|  _/ _ \ '__|
	 | |_) | |_| | | | | | | (_| | | \__ \ |_) | (_) | (_) | ||  __/ |
	 | .__/ \__, |_| |_| |_|\__,_|_|_|___/ .__/ \___/ \___/|_| \___|_|
	 | |     __/ |                       | |
	 |_|    |___/                        |_|
	                                       (v0.2)  |by Shams Parvez Arka|
	"""

banner()
disclimer()
mainpart()

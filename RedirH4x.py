# RedirH4x : RedirH4x is a Python-based vulnerability scanner designed to identify open redirect flaws in web applications. By analyzing URL parameters and detecting unvalidated redirects.
# Author : @40sp3l
import requests
from colorama import Fore
from art import *
import os
from subprocess import check_output
import re
import readline

if os.name == "posix":
   os.system('clear')
else:
   exit()

print(text2art("RedirH4x"))
print(Fore.YELLOW+"[INFO] ----> RedirH4x is designed to identify open redirect flaws in web applications."+Fore.WHITE)
print(Fore.BLUE+"[AUTHOR] ----> @40sp3l"+Fore.WHITE)
print()
try:
    target_url = input("[+] Enter Target URL: ")
except KeyboardInterrupt as e:
    print(e)
    exit()

domain = re.findall("[a-z]+.[a-z]+.[a-z]+", target_url)[1]

print(Fore.GREEN+"\n[INFO] RedirH4x Running... Make Sure To Test Manually"+Fore.WHITE)

try:
    urls = check_output(f"echo {domain} | waybackurls | grep -Ei '(redirect|url|return|dest|next|to|goto|continue|forward|ref|target|callback|nexturl|redirect_uri|destination|a)='", shell=True).decode().splitlines()
except:
    urls = []

for url in urls:
    try:
        response = requests.get(url, allow_redirects=False, timeout=5)
        status = response.status_code
        if 300 <= status < 400:
            print(Fore.YELLOW+f"\n[{status}] Redirect found -> {url}"+Fore.WHITE)
        else:
            pass
    except requests.RequestException as e:
        print(f"[ERROR] Could not fetch {url} - {e}")


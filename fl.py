#!/usr/bin/python3
#-*-coding:utf-8-*-
# Made With ❤️ By Dapunta

import sys,os,requests,json,time
from concurrent.futures import ThreadPoolExecutor as ThreadPool

def banner():
    print("""
  ___ ___    _    ___ ___ _____ 
 |_ _|   \  | |  |_ _/ __|_   _|
  | || |) | | |__ | |\__ \ | |  
 |___|___/  |____|___|___/ |_|  """)

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)

def login():
    os.system("rm -rf login.txt")
    os.system('clear')
    banner()
    toket = input("\n[•] Token : ")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        xd = open('login.txt', 'w')
        xd.write(toket)
        xd.close()
        print('\n[•] Login Successful')
        menu()
    except KeyError:
        print ("\n[!] Token Invalid")
        os.system('clear')
        login()

def menu():
    try:
        toket = open("login.txt","r").read()
    except KeyError:
        jalan("\n[!] Token Invalid")
        login()
    except IOError:
        jalan("\n[!] Token Invalid")
        login()
    os.system('clear')
    banner()
    print("\n[1] Get ID From Friendlist")
    print("[2] Get ID From Public")
    print("[3] Get ID From Followers")
    print("[0] Log Out")
    mn = input("\n[•] Select : ")
    if mn in [""]:
        jalan("\n[!] Fill In The Correct")
        menu()
    elif mn in ["1","01"]:
        teman()
    elif mn in ["2","02"]:
        public()
    elif mn in ["3","03"]:
        followers()
    elif mn in ["0","00"]:
        os.system("rm -rf login.txt")
        jalan("\n[!] Thanks For Using My Script")
        exit()
    else:
        jalan("\n[!] Fill In The Correct")
        menu()

def teman():
    try:
        toket = open("login.txt","r").read()
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        print ("\n[•] Name : %s"%(a['name']))
    except KeyError:
        jalan("\n[!] Token Invalid")
        login()
    except IOError:
        jalan("\n[!] Token Invalid")
        login()
    tampung=[]
    teman=[]
    lim = input("[•] Limit Dump : ")
    print ("\n")
    ada = requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(lim,toket))
    idi = json.loads(ada.text)
    for x in idi['data']:
        tampung.append(x['id'])
    for id in tampung:
        try:
            ada2 = requests.get('https://graph.facebook.com/%s/friends?access_token=%s'%(id,toket))
            idi2 = json.loads(ada2.text)
            try:
                for b in idi2['data']:
                    teman.append(b['id'])
            except KeyError:
            	print("[!] Private")
            print("[•]", id,"•",len(teman))
            teman.clear()
        except KeyError:
            print("[!] Akun Terkena Spam")
    kembali()

def public():
    it = input("\n[•] ID Public : ")
    try:
        toket = open("login.txt","r").read()
        otw = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,toket))
        a = json.loads(otw.text)
        print ("[•] Name : %s"%(a['name']))
    except KeyError:
        jalan("\n[!] Token Invalid")
        login()
    except IOError:
        jalan("\n[!] Token Invalid")
        login()
    tampung=[]
    teman=[]
    lim = input("[•] Limit Dump : ")
    print ("\n")
    ada = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(it,lim,toket))
    idi = json.loads(ada.text)
    for x in idi['data']:
        tampung.append(x['id'])
    for id in tampung:
        try:
            ada2 = requests.get('https://graph.facebook.com/%s/friends?access_token=%s'%(id,toket))
            idi2 = json.loads(ada2.text)
            try:
                for b in idi2['data']:
                    teman.append(b['id'])
            except KeyError:
            	print("[!] Private")
            print("[•]", id,"•",len(teman))
            teman.clear()
        except KeyError:
            print("[!] Akun Terkena Spam")
    kembali()

def followers():
    it = input("\n[•] ID Followers : ")
    try:
        toket = open("login.txt","r").read()
        otw = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,toket))
        a = json.loads(otw.text)
        print ("[•] Name : %s"%(a['name']))
    except KeyError:
        jalan("\n[!] Token Invalid")
        login()
    except IOError:
        jalan("\n[!] Token Invalid")
        login()
    tampung=[]
    teman=[]
    lim = input("[•] Limit Dump : ")
    print ("\n")
    ada = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(it,lim,toket))
    idi = json.loads(ada.text)
    for x in idi['data']:
        tampung.append(x['id'])
    for id in tampung:
        try:
            ada2 = requests.get('https://graph.facebook.com/%s/friends?access_token=%s'%(id,toket))
            idi2 = json.loads(ada2.text)
            try:
                for b in idi2['data']:
                    teman.append(b['id'])
            except KeyError:
            	print("[!] Private")
            print("[•]", id,"•",len(teman))
            teman.clear()
        except KeyError:
            print("[!] Akun Terkena Spam")
    kembali()

def kembali():
    input("\n[ Kembali ]")
    menu()

if __name__=="__main__":
	menu()

































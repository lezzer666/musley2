import libtvs
import time
import datetime
import random
import softlogo
from ss import session
from time import sleep
#import musley

class addr:
    openPorts = []
    ip = ""
    isActive = False
    rootPasswd = ""
    hostname = ""
    def __init__(self, openPorts, ip, isActive, rootPasswd, hostname):
        self.openPorts = openPorts
        self.ip = ip
        self.isActive = isActive
        self.rootPasswd = rootPasswd
        self.hostname = hostname
# Initializtation
evilcorp = addr(["tcp", "smb", "ssh"], "228.6.6.31", True, "123", "evil")
adresses = [evilcorp]
#r_files = [musley.passwords]
def nmap(ip='noip'):
    obj = None
    print("Starting Nmap 7.70 ( https://nmap.org ) at " + str(datetime.date.today()))
    time.sleep(4)

    for adress in adresses:
        if ip == adress.ip:
            obj  = adress
    
    if obj != None:
        print("Nmap scan report for " + ip)
        print("Host is up (" + libtvs.toFixed(random.random(), 3) + " lattency).")
        print("Not shown: " + str(1000 - len(adress.openPorts)) + " closed ports")
        print("PORT    STATE    SERVICE")
        if "smb" in adress.openPorts:
            print("139/smb   open    шindows")
        if "tcp" in adress.openPorts:
            print("8080      open    whoknows")
        if "ssh" in adress.openPorts:
            print("22        open    ssh")
    else:
        print("Nmap done: 1 IP addresses (0 hosts up) scanned in " + libtvs.toFixed(random.random(), 3) + " seconds")

def ssh(ip='noip'):
    if ip == 'noip':
        print('''
usage: ssh ip''')
    obj = None
    print("Connecting to " + ip + " on port 22")

    for adress in adresses:
        if ip == adress.ip and "ssh" in adress.openPorts:
            obj = adress
    
    time.sleep(3)

    if obj != None:
        if input("root@" + obj.hostname + " password: ") == obj.rootPasswd:
            time.sleep(1)
            print("Starting shell")
        else:
            time.sleep(1)
            print("Incorrect password for root@" + obj.hostname)
    else:
        print("Cant resolve host " + ip)

def curl(addr):
    for r_file in r_files:
        if addr == r_file.r_path:
            session["cur_dir"].files.append(r_file)
            sleep(1)
            print("Downloaded.")
        else:
            print("Can't reach the target.")

def mkdir(name):
        name=musley.dir(name, [], [], session['cur_dir'])
        try:
            eval(session["cur_dir"]).subdirs.append(name)
        except:
            eval(musley.shortcuts[session["cur_dir"]]).subdirs.append(name)
        sleep(0.2)

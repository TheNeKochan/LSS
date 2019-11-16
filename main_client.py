from requests.auth import HTTPBasicAuth
from mac2ip import *
import subprocess
import Intervals
import requests
import hashlib
import socket
import json
import time
import os


cfg = json.load(open("config_client.json"))
server_ip = mac2ip(cfg['settings']['server']['mac'])

def checker():
    configfile = open("config_client.json", 'r')
    confighash = hashlib.md5(configfile.read().encode()).hexdigest()
    configfile.close()
    nc = socket.socket()
    nc.connect((server_ip, 8080))
    nc.send(b"hash")
    newconfighash = nc.recv(64).decode()
    if not confighash == newconfighash:
        nc.send(b"config")
        newconfig = nc.recv(1024).decode()
        nc.close()
        print(newconfighash, newconfig)
        configfile = open("config_client.json", 'w')
        configfile.write(newconfig)
        configfile.close()
    else:
        nc.send(b"END")
        nc.close()

read, write = os.pipe()
os.write(write, str(os.getpid()).encode())
os.close(write)

Intervals.setinterval(checker, 1000, 0)
stream = subprocess.Popen("python main.py", stdin=read)
time.sleep(360)
requests.request("GET", "http://localhost:9000/sh?pid=" + str(os.getpid()), auth=HTTPBasicAuth('user', 'Simple_pass'))
print("Killed")
time.sleep(10)
# at the end of program
Intervals.delinterval(0)

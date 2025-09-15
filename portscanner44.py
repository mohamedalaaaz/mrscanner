import  socket
from termcolor import colored

sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#socket.setdefaulttimeout(2)

host =input("[*]enter host to scan:!]")


def portscanne (port):
    if sock.connect_ex((host,port)):
        print(colored("port is close %d " %(port),"red"))

    else:
        print(colored("port is open %d" % (port),"green"))

for port in range(1,1000):


    portscanne(port)

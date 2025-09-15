import  socket

sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(2)
port=int(input("[*] enter port to scan"))
host =input("[*]enter host to scan:!]")


def portscanne (port):
    if sock.connect_ex((host,port)):
        print("port is close %d " %(port))

    else:
        print("port is open %d" % (port))

for port in range(1,100):


    portscanne(port)

from socket import *

import optparse
from threading import *


def connscan(tgthost,tgtport):
    try:
        sock=socket(AF_INET,SOCK_STREAM)
        sock.connect((tgthost,tgtport))
        print("%d /tcp open"%tgtport)
    except:
        print("%d /tcp closed"%tgtport)
    finally:
        sock.close()


def portscan(tgthost,tgtport):
    try:
        tgtip=gethostbyname(tgthost)
    except:
        print('unknown host s%' %tgthost)

    try:
        tgtname=gethostbyaddr(tgtip)
        print(tgtname[0])

    except:
        print("scan results"+tgtip)

    setdefaulttimeout(1)
    for tgtport in tgtport:
        t=Thread(traget=connscan,args=(tgthost,int(tgtport)))
        t.start()


def main():
    parser =optparse.OptionParser('usage of program: '+'-H <target host > -p <target port>')
    parser.add_option('-H',dest='tgthost',type='string',help='specify target host')
    parser.add_option('-p', dest='tgtport', type='string', help='specify target ports seperated by coma ')
    (options,args)=parser.parse_args()
    tgthost=options.tgthost
    tgtport=str(options.tgtport).split(',')
    if ((tgthost == None )| (tgtport[0] == None)):
        print(parser.usage)
        exit(0)

if __name__ == '__main__':
    main()

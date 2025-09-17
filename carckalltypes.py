import hashlib

def tryopen(worldlist):
    global pass_file
    try:
        pass_file=open(worldlist,'r')
    except:
        print("[!!] no such file at that path")


passhash=input("enter md5 hash value")

worldlist=input("[+] enter path to password file")
tryopen(worldlist)

for word in pass_file:
    print("[-] tring :"+word.strip("\n"))
    enc_wrd=word.encode('utf-8')
    md5digest=hashlib.md5(enc_wrd.strip().hexdigest())

    if md5digest ==passhash:
        print("[+] password found" + word )
        exit(0)



print("[!!] password not in list " )
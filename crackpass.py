from urllib.request import urlopen
import hashlib




shahash=input("[+] enter shal hash value")

passlist=str(urlopen('https://gist.githubusercontent.com/richardkundl/b68afdcf68240dcff50a/raw/9d3599897308553ba3fcd24baef5a4cb8f6f57b6/10k-common-passwords').read(),'utf-8')
for i in passlist.split('\n'):
    hashguess=hashlib.sha1(bytes(i,'utf-8')).hexdigest()
    if hashguess ==shahash:
        print("[+] the password is " +str(i))
        quit()
    else:
        print("[-] password guss  "+ str(i)+ " "+"does not match")
print("password not in passwordlist")
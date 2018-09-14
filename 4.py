# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib.request

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

req = urllib.request

a = '12345'
for i in range(400):
    d = req.urlopen(url + a)
    a = d.read().split()[-1].decode('utf-8')
    print(a)

#peak.html이 나옴
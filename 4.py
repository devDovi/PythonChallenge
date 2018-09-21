# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib.request

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

req = urllib.request

a = '12345'
for i in range(400):
    d = req.urlopen(url + a)
    data = d.read().decode('utf-8')
    a = data.split()[-1]
    print(data)

#peak.html이 나옴
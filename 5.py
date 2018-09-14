# http://www.pythonchallenge.com/pc/def/peak.html
# image name is peakhell.jpg
# <peakhell src="banner.p"></peakhell>
# peakhell -> pickle

import pickle
from urllib.request import urlopen

data = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

t = (' ', 5)
print([for a, b in t])

#for line in data:
    #print([k * (v+1) for k, v in line])
    #print(''.join([k * v for k, v in line]))

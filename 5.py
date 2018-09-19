# http://www.pythonchallenge.com/pc/def/peak.html
# image name is peakhell.jpg
# <peakhell src="banner.p"></peakhell>
# peakhell -> pickle

import pickle
from urllib.request import urlopen

data = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

t = (' ', 5)

for line in data:
    print(''.join([k * v for k, v in line]))

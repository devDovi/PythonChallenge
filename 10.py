# http://www.pythonchallenge.com/pc/return/bull.html
# 
# # Native

a = '1'
b = ''

for i in range(0, 3):
    j = 0
    k = 0
    while j < len(a):
        while k < len(a) and a[k] == a[j]: k += 1
        b += str(k-j) + a[j]
        j = k
        print(j, k, b)
    print (b)
    a = b
    b = ''

print (len(a))

# Using Regex

import re
x = "1"
for n in range(30):
    x="".join([str(len(j) + 1)+i for i, j in re.findall(r"(\d)(\1*)", x)])

print(len(x))
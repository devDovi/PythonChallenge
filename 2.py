f = open('ocr.txt','r')
data = f.read()
answer = ''

for i in data:
    if i.isalpha():
        answer += i

print(answer)

f.close()

# http://www.pythonchallenge.com/pc/def/ocr.html
# equality
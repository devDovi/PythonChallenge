# http://www.pythonchallenge.com/pc/def/channel.html
# Comment <!-- <-- zip -->
# goto zip.html -> channel.zip
# readme.txt : welcome to my zipped list. hint1: start from 90052 hint2: answer is inside the zip
# 46145.txt : Collect the comments.
# ZipInfo.comment -> individual member's comment
# 
# http://www.pythonchallenge.com/pc/def/hockey.html
# OXYGEN - HOCKEY

import zipfile

zf = zipfile.ZipFile("channel.zip")
f = open("channel/90052.txt",'r')
fileName = f.read().replace("Next nothing is ", "")
print (zf.getinfo("90052.txt").comment.decode('utf-8'), end='')

while fileName:
    filePath = "channel/"+fileName+".txt"
    f = open(filePath)   
    fileName = f.read().replace("Next nothing is ","")   
    print (zf.getinfo(fileName+".txt").comment.decode('utf-8'), end='')
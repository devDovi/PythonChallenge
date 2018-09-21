# http://www.pythonchallenge.com/pc/return/mozart.html

from PIL import Image
import numpy as np

image = Image.open('mozart.gif')

print([x for x in image.histogram() if x % image.height == 0 and x != 0])
# [2400] (pink pixel shows 2400 times / and exists every row)

print(image.histogram().index(2400))
# 195 / pink pixel's RGB value (0 ~ 255)

# tmp.frombytes(bytes([195] * (tmp.height * tmp.width)))
# tmp.show()
# Check pixel's value

shifted = [bytes(np.roll(row, -row.tolist().index(195)).tolist()) for row in np.array(image)]
# Shift image's row by numpy.roll()

Image.frombytes(image.mode, image.size, b''.join(shifted)).show()
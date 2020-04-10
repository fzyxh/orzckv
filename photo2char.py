from PIL import Image
inPath = input('path for process:')
WIDTH = int(input('How long you want for width:'))
HEIGHT = int(input('How long you want for height:'))
outPath = input('path for save:')
print('processing,please wait')
char = u'WM%&@-.'
demarcation = 128
def limit(x,start,end):
	if(x <= start):
		return start
	if(x >= end):
		return end
	return x
def getchar(r,g,b):
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
	std = int(demarcation / len(char))
	return char[limit(int(gray / std),0,len(char) - 1)]
if(__name__ == '__main__'):
	img = Image.open(inPath).convert('RGB')
	img = img.resize((WIDTH,HEIGHT),Image.NEAREST)
	text = ''
	for i in range(HEIGHT):
		for j in range(WIDTH):
			r,g,b = img.getpixel((j,i))
			text += getchar(r,g,b)
		text += '\n'
	with open(outPath,'w') as file:
		file.write(text)




'''# -*- coding:utf8 -*-
 
import cv2
 
charSize = 2#字符尺寸
 
string = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
count = len(string)
img = cv2.imread('ckv1.jpg')
u, v, _= img.shape
c = img*0 + 255
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
for i in range(0, u, 6):
    for j in range(0, v, 6):
        pix = gray[i, j]
        b, g, r = img[i, j]
        zifu = string[int(((count - 1) * pix) / 256)]
        cv2.putText(c, zifu, (j, i), cv2.FONT_HERSHEY_COMPLEX, charSize, (int(b), int(g), int(r)), 1)
 
cv2.imwrite('output.png', c)
'''

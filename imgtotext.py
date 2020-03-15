import cv2
from PIL import Image
from pytesseract import *
import re

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

record = False
label=1
texts=[]

def strTotTxt(txtName, outText):
    with open(txtName+'.txt', 'a', encoding='utf-8') as f:
        f.write(outText)

while True:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    key = cv2.waitKey(33)

    if key == 27:
        break
    elif key == 99:
        print("캡쳐")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        cv2.imwrite("C:\dev\py\img\\" + str(label) + ".jpg", gray)
        
        img = cv2.imread('img/'+str(label)+'.jpg')
        text = pytesseract.image_to_string(img,lang='eng')
        print(text)
        
        if text in texts:
            print("중복!!!")    
        else:
            texts.append(text)
            strTotTxt('result.txt', text+'\n')
        
        label+=1

capture.release()
cv2.destroyAllWindows()

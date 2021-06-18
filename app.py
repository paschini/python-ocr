# the most basic example to get text out of an image

import pytesseract
import cv2

# img = cv2.imread(r'resources/testCC/NZ-216199115-CC-CC_216199115_1615189719991_0.jpg')
img = cv2.imread(r'resources/testCC/visaKlarna.png')


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(img)

print(text)

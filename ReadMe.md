# Python OCR

## Credit card number detection and masking

Uses Python3, OpenCV and Tesseract.  
Very simple for now.  

Trys to match the credit card number against a reference image.   
Also return Tesseract results.

The reference image has all possible digits, written in the OCR-A font, commonly used in credit cards.  
More adjustment is needed to get better results for these cards.

Fails if it doesn't find all 16 digits.

### TODO:
- [ ] mask all but last 4 digits
- [ ] improve detection of other cards
- [ ] try to detect the card's position in the image and if needed rotate it  
- [ ] try to match using a vertical reference image as alternative?
- [ ] train opencv/tesseract for different card formats?
- [ ] add support to extract more information, like name
  
- [ ] fix window not opening with the drawn over image result

----

## How to run:
Install all libraries:
``pip install opencv-contrib-python imutils pytesseract``

creditcards.py:
``python3 creditcards.py``

Example fake cards and reference image included in ``resources``.

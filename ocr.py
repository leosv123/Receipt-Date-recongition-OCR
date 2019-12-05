from PIL import Image
import pytesseract
import argparse
import cv2
import os

image = cv2.imread('images/02d54805.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", gray)

#if args["preprocess"] == "thresh":
#	gray = cv2.threshold(gray, 0, 255,
#		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#elif args["preprocess"] == "blur":
#	gray = cv2.medianBlur(gray, 3)

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print("predicted after FasterCNN(ResNet50)+Google Tesseract :"+ str(text))


# show the output images
# cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)
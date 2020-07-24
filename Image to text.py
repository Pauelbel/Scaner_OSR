# Установка языковых пакетов для tesseract https://ru.stackoverflow.com/questions/1015468/%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-%D1%8F%D0%B7%D1%8B%D0%BA%D0%BE%D0%B2%D1%8B%D1%85-%D0%BF%D0%B0%D0%BA%D0%B5%D1%82%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-tesseract

from cv2 import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("C:/Users/pvbel/Desktop/Scaner_osr/pic.PNG")

text = pytesseract.image_to_string(img, lang="rus+eng")

print(text)
from PIL import Image

import  pytesseract

im = Image.open("bride.jpg") # abrir imagen 

textt=pytesseract.image_to_string(im,lang="eng")   # Extraer texto de la imagen 

print(text)

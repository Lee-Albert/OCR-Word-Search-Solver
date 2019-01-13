from PIL import Image
import pytesseract

im = Image.open("pic.png")
basewidth = 6000
wpercent = (basewidth/float(im.size[0]))
hsize = int((float(im.size[1])*float(wpercent)))
im = im.resize((basewidth,hsize), Image.ANTIALIAS)

text = pytesseract.image_to_string(im, lang = "eng")

print(text)
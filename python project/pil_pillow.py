__author__ = '绍文'

from PIL import Image, ImageDraw, ImageFont

im = Image.open("paul.jpg")
picture_width, picture_height = im.size
text = "123"
draw = ImageDraw.Draw(im)
font = ImageFont.truetype("STXIHEI.TTF", 25)
w_font, h_font = draw.textsize(text,font)
draw.text((picture_width - w_font, 0), text, fill="red", font=font)
im.save("output.jpg")
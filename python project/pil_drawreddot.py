__author__ = '绍文'

from PIL import Image, ImageDraw, ImageFont

im = Image.open("paul.jpg")
draw = ImageDraw.Draw(im)
w_width, h_height = im.size
text = "19"
font = ImageFont.truetype("STXIHEI.TTF", 25)
w_font, h_font = draw.textsize(text,font)
draw.ellipse(((w_width - w_font, 3), (w_width, w_font + 3)), fill="#D00000", outline=None)
draw.text((w_width - w_font, 0), text, fill="white", font=font)
size = (128, 128)
im.thumbnail(size)
im.save("reddot.jpg")
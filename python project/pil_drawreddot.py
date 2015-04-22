__author__ = '绍文'

from PIL import Image, ImageDraw, ImageFont

im = Image.open("005.jpg")
draw = ImageDraw.Draw(im)
w_width, h_height = im.size
text = "19"
font = ImageFont.truetype("STXIHEI.TTF", 300)
w_font, h_font = draw.textsize(text,font)
draw.ellipse(((w_width - w_font, 30), (w_width, w_font + 30)), fill="#D00000", outline=None)
draw.text((w_width - w_font, 0), text, fill="white", font=font)
size = (128, 128)
im.thumbnail(size)
im.save("reddot.jpg")
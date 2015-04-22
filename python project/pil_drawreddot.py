__author__ = '绍文'

from PIL import Image, ImageDraw, ImageFont

im = Image.open("007.jpg")
w_width, h_height = im.size
draw = ImageDraw.Draw(im)
text = "19"
font = ImageFont.truetype("STXIHEI.TTF", 30)
w_font, h_font = draw.textsize(text,font)
draw.ellipse(((w_width - w_font, 3), (w_width, w_font + 3)), fill="#D00000", outline=None)
draw.text((w_width - w_font, 0), text, fill="white", font=font)
im.save("reddot.jpg")
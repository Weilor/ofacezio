__author__ = '绍文'

from PIL import Image, ImageDraw, ImageFont

im = Image.open("007.jpg")
w_width, h_height = im.size
back_size = (w_width + 20, h_height + 20)
im_back = Image.new("RGBA", back_size, color=(255, 255, 255))
b_width, b_height = im_back.size
im_back.paste(im, (10, 10))
draw = ImageDraw.Draw(im_back)
text = "19"
font = ImageFont.truetype("STXIHEI.TTF", 30)
w_font, h_font = draw.textsize(text,font)
draw.ellipse(((b_width - w_font, 3), (b_width, w_font + 3)), fill="#D00000", outline=None)
draw.text((b_width - w_font, 0), text, fill="white", font=font)
im_back.save("reddot.jpg")
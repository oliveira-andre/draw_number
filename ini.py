from PIL import Image

from PIL import ImageFont
from PIL import ImageDraw

img = Image.new('RGB', (1000, 500), (250,250,250))
data = img.load()
number = "666"

for x in range(img.size[0]):
    for y in range(img.size[1]):
        data[x,y] = (
                x % 50,
            y % 50,
            (x**2-y**2) % 255,
        )

draw = ImageDraw.Draw(img)
font = ImageFont.truetype("OpenSans-Regular.ttf", 400)
draw.text((180, -30), number, (0,0,0), font=font)

img.save('image.png')

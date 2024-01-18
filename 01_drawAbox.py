# importing image object from PIL
import random
from PIL import Image, ImageDraw

#w, h = 220, 190
#shape = [(40, 40), (w - 10, h - 10)]

# creating new Image object
for i in range(10):
    
    print(i)
    img = Image.new("RGB", (1000, 1000), (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)))

# create line image
#img1 = ImageDraw.Draw(img)
#img1.line(shape, fill ="red", width = 0)


    img.save('boxes/'+str(i)+'_p'+'.jpg')

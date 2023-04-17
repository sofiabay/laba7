from PIL import Image
from PIL import ImageFilter

images = []

for i in range (1, 6):
    images.append(str(i) + '.JPG')

for img in images:
    image = Image.open(img)
    img_g = image. filter(ImageFilter.CONTOUR)
    img_g.save('kartinki/' + str(img))
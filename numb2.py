from PIL import image

image = Image.open('cat.JPG')
res_img1 = image.reduce(3)
res_img1 = save('Уменьшенная картинка.JPG')

res_img2 = image.transpose(Image.FLIP_LEFT_RIGHT)
res_img2.save('Отзеркалено горизонтально.JPG)

res_img3 = image.transpose(Image.FLIP_TOP_BOTTOM)
res_img3.save('Отзеркалено вертикально.JPG')

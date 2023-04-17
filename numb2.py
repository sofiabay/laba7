from PIL import image

image = Image.open('1.png')
res_img1 = image.reduce(3)
res_img1 = save('Уменьшенная картинка.png')

res_img2 = image.transpose(Image.FLIP_LEFT_RIGHT)
res_img2.save('Отзеркалено горизонтально.png)

res_img3 = image.transpose(Image.FLIP_TOP_BOTTOM)
res_img3.save('Отзеркалено вертикально.png')

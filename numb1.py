from PIL import image

image = Image.open('cat.JPG')
image. show ()
print('Формат изображения: ' , image.format)
print('Размер изображения: ' , image.size)
print('Цветовая модель изображения: ' , image.mode)


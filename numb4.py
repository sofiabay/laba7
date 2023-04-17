from PIL import Image

def watermark_photo(input_image_path, output_image_path, watermark_image_path, position):
    images = []
    for img in images:
    image = Image.open(img)
    watermark = Image.open(toypuddle.JPG)
    image.paste(watermark, position)
    image.show()
    image.save('watermark/' + str(img))
    watermark_with_photo(img, 'dogeyes_watermarked2.JPG', 'watermark.JPG', position=(0,0))
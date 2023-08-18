from PIL import Image

HEIGHT = 100
WIDTH = 100

resized_image = 'resized.jpg'

size = (HEIGHT, WIDTH)
image = Image.open(r'convo.jpg')

r_image = image.resize(size, resample=Image.BILINEAR)
r_image.save(resized_image)

image = Image.open(resized_image)
print(image.size)

from PIL import Image, ImageFilter, ImageOps

img = Image.open('./pokedex/6.1 astro.jpg')

# print(img.size)
new_img = img.resize((400, 400))
new_img.thumbnail((400, 200))
# thumbnail method resize a image object
# in place and keep aspect ratio in the meantime.
new_img.save('resized_astro.png', 'png')

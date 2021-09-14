from PIL import Image, ImageFilter, ImageOps

img = Image.open('./pokedex/4.1 squirtle.jpg')
# img.show()
# rotated_img = img.rotate(180)
# rotated_img.save('rotated_img.png', 'png')
# resized_img = img.resize((300, 300))
# resized_img.save('resized_img.png', 'png')
box = (100, 100, 400, 400)
crop_img = img.crop(box)
crop_img.save('crop_img.png', 'png')

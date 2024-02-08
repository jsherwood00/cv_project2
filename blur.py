from PIL import Image, ImageFilter
im = Image.open('vending_machine.jpg')
im2 = im.filter(ImageFilter.GaussianBlur(70))
im2.show()
im2.save('vending_machine_blur_70.jpg')
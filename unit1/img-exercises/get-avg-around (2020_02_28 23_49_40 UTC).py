from PIL import Image

img = Image.open("luther.jpg")

new_image = image.EmptyImage(input_image.getWidth(), input_image.getHeight())    
#width = x
#height = y
print(img.getWidth())
print(img.getHeight())
test = 0
for row in range(1, img.getWidth() - 1):
    for col in range(1, img.getHeight() - 1):
        newx = sum(row -1, row + 1, row) / 3
        newy = sum(col -1, col + 1, col - 1) / 3

        old_pixel = img.getPixel(col, row)
        new_image.SetPixel(newx, newy, old_pixel)

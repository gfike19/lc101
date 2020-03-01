import image

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)

        red = p.getRed()
        green = p.getGreen()
        blue = p.getBlue()
        
        grey=(red+green+blue)/3

        newpixel = image.Pixel(grey, grey, grey)

        newimg.setPixel(col, row, newpixel)

newimg.draw(win)
win.exitonclick()


import image

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

def grayscale(img):
    for col in range(img.getWidth()):
        for row in range(img.getHeight()):
            p = img.getPixel(col, row)
            
            red = p.getRed()
            green = p.getGreen()
            blue = p.getBlue()
            
            grey=(red+green+blue)/3
            if grey>125:
                grey=255
            else:
                grey=0
            newpixel = image.Pixel(grey, grey, grey)
            newimg.setPixel(col, row, newpixel)

grayscale(img)
newimg.draw(win)
win.exitonclick()




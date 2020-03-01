import image

def double(old_image):
    old_w = old_image.getWidth()
    old_h = old_image.getHeight()

    new_img = image.EmptyImage(old_w * 2, old_h * 2)
    for row in range(old_h):
        for col in range(old_w):
            old_pixel = old_image.getPixel(col, row)

            new_img.setPixel(2*col, 2*row, old_pixel)
            new_img.setPixel(2*col+1, 2*row, old_pixel)
            new_img.setPixel(2*col, 2*row+1, old_pixel)
            new_img.setPixel(2*col+1, 2*row+1, old_pixel)

    return new_img

def smooeth(input_image):
    new_image = image.EmptyImage(input_image.getWidth(), input_image.getHeight())    
    #width = y
    #height = x
    for i in range(1, img.getWidth() - 1):
        for j in range(1, img.getHeight() - 1):
            newx = old_image.

    

def main():
    img = image.Image("luther.jpg")
    win = image.ImageWin(img.getWidth() * 2, img.getHeight() * 2)

    big_img = double(img)
    big_img.draw(win)

    win.exitonclick()

if __name__ == "__main__":
     main()



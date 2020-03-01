import image
import sys

# Set the timeout to a larger number if timeout is occuring.
sys.getExecutionLimit(30000)

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

for x in range(0, img.getWidth()):
    for y in range(0, img.getHeight()):
        old_p = img.getPixel(x, y)
        center=img.getPixel(x,y)
        right=img.getPixel(201,120)
        left=img.getPixel(199,120)
        up=img.getPixel(200,121)
        down=img.getPixel(200,119)
        
        center_Red=center.getRed()
        center_Green=center.getGreen()
        center_Blue=center.getBlue()
        
        new_c_red=center_Red*8
        new_c_green=center_Green*8
        new_c_blue=center_Blue*8
        
        right_Red=right.getRed()
        right_Green=right.getGreen()
        right_Blue=right.getBlue()
        
        new_r_red=right_Red*3
        new_r_green=right_Green*3
        new_r_blue=right_Blue*3

        
        left_Red=left.getRed()
        left_Green=left.getGreen()
        left_Blue=left.getBlue()
        
        new_l_red=left_Red*3
        new_l_green=left_Green*3
        new_l_blue=left_Blue*3
        
        up_Red=up.getRed()
        up_Green=up.getGreen()
        up_Blue=up.getBlue()
        
        new_u_red=up_Red*3
        new_u_green=up_Green*3
        new_u_blue=up_Blue*3
        
        down_Red=down.getRed()
        down_Green=down.getGreen()
        down_Blue=down.getBlue()
        
        new_d_red=down_Red*3
        new_d_green=down_Green*3
        new_d_blue=down_Blue*3
        
        red_total=(new_c_red+new_u_red+new_d_red+new_r_red+new_l_red)/20
        green_total=(new_c_green+new_u_green+new_d_green+new_r_green+new_l_green)/20
        blue_total=(new_c_blue+new_u_blue+new_d_blue+new_r_blue+new_l_blue)/20
        
        center.setRed(red_total)
        center.setGreen(green_total)
        center.setBlue(blue_total)
        
        new_p=image.Pixel(old_p.
        
        
newimg.draw(win)
win.exitonclick()
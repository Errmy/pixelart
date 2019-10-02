
from PIL import Image
import sys

pixelarea = 16
arguments = len(sys.argv) - 1
if arguments == 0:
    print("No arguments entered.")
else:
    imagefile = sys.argv[1]
    splitedimgf = imagefile.rsplit(".",1)
    if splitedimgf[1] != "jpg":
        print("File is not a jpg.")
    else:
        print("Processing image " + imagefile + ".")
        im = Image.open(imagefile)
        #print(im.format)
        imagewidth = im.width
        imageheight = im.height
        #print('width = ' + str(imagewidth) + ' height = ' + str(imageheight))
        rgb_im = im.convert('RGB')
        pixelim = Image.new('RGB', (imagewidth, imageheight), "black")

        r = [[j for j in range(pixelarea)] for i in range(pixelarea)]
        g = [[j for j in range(pixelarea)] for i in range(pixelarea)]
        b = [[j for j in range(pixelarea)] for i in range(pixelarea)]
        #print(range(0,pixelarea))

        for h in range(pixelarea,im.height+1,pixelarea):
            for w in range(pixelarea,im.width+1,pixelarea):
                raverage = 0
                gaverage = 0
                baverage = 0
                for x in range(0,pixelarea):
                    
                    for y in range(0,pixelarea):
                        r[x][y], g[x][y], b[x][y] = rgb_im.getpixel((w-x-1, h-y-1))
                        raverage = raverage + r[x][y]
                        gaverage = gaverage + g[x][y]
                        baverage = baverage + b[x][y]
                raverage = int(raverage/(pixelarea*pixelarea))
                gaverage = int(gaverage/(pixelarea*pixelarea))
                baverage = int(baverage/(pixelarea*pixelarea))
                for x in range(0,pixelarea):
                    for y in range(0,pixelarea):
                        pixelim.putpixel((w-x-1, h-y-1),(raverage, gaverage, baverage))

        pixelim.save(splitedimgf[0]+"_pixelart.jpg")

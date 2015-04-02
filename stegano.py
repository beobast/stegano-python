#!/usr/bin/env python
 
import sys
from PIL import Image
 
def hide(coverImage, stegoImage):
    imageSource = Image.open(coverImage).convert('RGB')
    imageToHide = Image.open(stegoImage).convert('RGB')
    width, height = imageSource.size
    width2, height2 = imageToHide.size
 
    if width != width2 or height != height2 :
        sys.exit('Error, images must have same size (width x height)')
 
    imageResult = Image.new('RGB', (width,height))
 
    for x in range(width):
        for y in range(height):
            pixelSource = imageSource.getpixel((x,y))
            pixelToHide = imageToHide.getpixel((x,y))
            pixelResult = ()
             
            for a, b in zip(pixelSource, pixelToHide):
                pixelResult += (a & 248 | b >> 5),
 
            imageResult.putpixel((x,y),pixelResult)
 
    imageResult.save('result.png')
 
def reveal(image):
    imageSource = Image.open(image).convert('RGB')
    width, height = imageSource.size
 
    imageResult = Image.new('RGB', (width,height))
 
    for x in range(width):
        for y in range(height):
            pixelSource = imageSource.getpixel((x,y))
            pixelResult = ()
 
            for a in pixelSource:
                pixelResult += (a << 5 & 255),
 
            imageResult.putpixel((x,y),pixelResult)
 
    imageResult.save('revealed.png')
 
def help():
    print ('Usage: ')
    print ('\tHide: stegano.py <coverImage> <secretImage>')
    print ('\tReveal: stegano.py <image>')
 
def main():
 
    nbArgs = len(sys.argv)

    if nbArgs != 2 and nbArgs != 3: sys.exit(help())
 
    try:
        if nbArgs == 3:
            hide(sys.argv[1], sys.argv[2])
        elif nbArgs == 2:
            reveal(sys.argv[1])
    except Exception as e:
        sys.exit(e)
 
    return 0
 
if __name__ == '__main__':
    main()

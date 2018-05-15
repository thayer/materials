
# coding: utf-8

# In[ ]:

'''
Erfan Azad <erfan@dartmouth.edu>
Date: May 14, 2017

This script is to go through all the images in a directory and resize, crop and pad them 
in order to make them all the same size, but without stretching.
'''


# In[10]:

import os
from PIL import Image


# In[17]:

def main():
    fromDir = "./matImages"
    toDir = "./matImagesCropped"
    desiredWidth = 1500;
    desiredHeight = 1500;

    for filename in os.listdir(fromDir):
        if filename.split(".")[1] in ["jpg", "JPG"]:
            img = Image.open(fromDir+"/"+filename)
            width = img.size[0]
            height = img.size[1]
            assert(width == desiredWidth) # the photo is pre-prosessed (with preview) to have width of 1500px
            if height < desiredHeight:
                print("padding")
                #pad it
                vertical_padding = (desiredHeight - height) / 2
                horizontal_padding = 0
                img_new = img.crop(
                    (
                        -horizontal_padding,
                        -vertical_padding,
                        width + horizontal_padding,
                        height + vertical_padding
                    )
                )
                img_new.save(toDir+"/"+filename)
            elif height > desiredHeight:
                print("cropping")
                vertical_cropping = (height - desiredHeight) / 2
                horizontal_cropping = 0
                img_new = img.crop(
                    (
                        +horizontal_cropping,
                        +vertical_cropping,
                        width - horizontal_cropping,
                        height - vertical_cropping
                    )
                )
                img_new.save(toDir+"/"+filename)

    


# In[ ]:

if __name__ == "__main__":
    main()


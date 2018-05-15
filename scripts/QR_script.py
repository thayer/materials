
# coding: utf-8

# ### Script to take an image of QR code and saves it again in another image with the filename included in it

# In[1]:

from PIL import Image, ImageDraw, ImageFont
import qrcode
import time


# In[43]:

def makeQR(url):
    '''
    talkes a url string and creates a QR code form it.
    
    Args:
        url: S string containing the url to make qrcode for
        
    Returns:
        An image (qrcode.image.pil.PilImage)
    '''
#     img = qrcode.make(url)
#     img.show()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(url)
    img = qr.make_image()
    return img


# In[53]:

def addText2Image(img, text):
    
    img = img.convert('RGBA')
    percentIncrease = 10.0                                     # Make a bigger canvas for both QR and the text
    height,width = img.size
    newHeight = int(height + (percentIncrease/100)*height)
    newWidth = int(width + (percentIncrease/100)*width)        # Offset the QR to be center horizontally
    offset1_x = (newWidth - width)/2 
    offset1_y = 0
    
    base = Image.new('RGBA', (newHeight, newWidth),(255,255,255,255))  # Create the new canvas
    base.paste(img, (offset1_x,offset1_y))                             # Add QR to canvas
    
    fontSize = 50
    font = '/Library/Fonts/Arial Bold.ttf'
    offset2_x = 0.35*newWidth
    offset2_y = 0.88*newHeight
    fnt = ImageFont.truetype(font, fontSize)
    
    draw = ImageDraw.Draw(base)                                        # Create a drawable from canvas
    draw.text((offset2_x,offset2_y), text, font=fnt, fill=(0,0,0,255)) # Draw the text on canvas
    return base
    


# In[56]:

def main():
    tic = time.clock()
    productNumber_start = 3001
    productNumber_end = 3208
    savePath = "./QRs"
    print("Saving path: {}".format(savePath))
    for i in range(productNumber_start,productNumber_end+1):
        QRimg = makeQR("http://engineering.dartmouth.edu/materials-library/products/{}.html".format(i)) #QR code url
        resultImage = addText2Image(QRimg, str(i))
        filename = "{}/{}.png".format(savePath, i)
        resultImage.save(filename)
        print("{}: Saved!".format(filename))
    toc = time.clock()
    print("Finished creating {} QR codes in {:.2f} seconds!".format((productNumber_end-productNumber_start), (toc-tic)))


# In[57]:

if __name__ == "__main__":
    main()


# In[ ]:




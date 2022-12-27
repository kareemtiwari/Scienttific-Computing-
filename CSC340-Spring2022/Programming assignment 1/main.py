import cv2
import numpy as np

#read in image (in the same folder)
image = cv2.imread("cones1.png")
#read in image(in subfolder)
## image = cv2.imread("img/cones1.png")

#get size of image
numRows = image.shape[0] # height of image
numCols = image.shape[1] # width of image

#create an empty image
emptyIm = np.zeros((numRows,numCols, 3), np.float32) # size,data type #Programing Lab1#

#iterate over a;; the pixels of your image
for i in range(numRows): # iterate over the height of the image, y-coordinates
    for j in range(numCols): # iterate over the width of the image, x-coordinates

        #access va;ues at pixel:
        emptyIm[i][j][0] = image[i][j][0] # blue value stored at pixel(i,j)
        emptyIm[i][j][1] = image[i][j][1]# green value stored at pixel(i,j)
        emptyIm[i][j][2] = image[i][j][2]# red value stored at pixel(i,j)
        #grayscle the image
        grayVal = (float(image([i][j][0])) + float(image[i][j][1]) + float(image[i][j][2]))/3.0
        emptyIm[i][j][0] = grayVal
        emptyIm[i][j][1] =grayVal
        emptyIm[i][j][2] = grayVal
        
        image[i][j][0] = 0
        
        #image[i][j][2] = 0
        

        emptyIm[i][j][0] = image[i][j][0] # copy blue channel at each [ixel from original image to a new image you made

#displaying an image
cv2.imshow("new image",emptyIm/255.0)

#keep image open
#cv2.waitkey(0)
#cv2.destroyAllWindows()

## Save and image
#same folder as code

cv2.imwrite("savedImg.png", emptyIm)

#in a subfolder called"results"

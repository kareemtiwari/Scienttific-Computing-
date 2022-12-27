import cv2
import numpy as np

image = cv2.imread("cones1.png")

numRows = image.shape[0]
numCols = image.shape[1]
size1= 2*numRows
size2=2*numRows
emptyIm = np.zeros((size1, size2, 3),np.float32)
for i in range(numRows):C
    for j in range(numCols):

        emptyIm[i+150][j+150][0] = image[i][j][0]
        emptyIm[i+150][j+150][1] = image[i][j][1]
        emptyIm[i+150][j+150][2] = image[i][j][2]

cv2.imshow("new image", emptyIm/255.0)
cv2.imwrite("newcones1.png", emptyIm/255.0) 


                    
 

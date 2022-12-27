##Kareem Tiwari
##HarrisCorners


####
# Create empty images that are the same size as the original image
# Create Ix, Iy,Ixx,Iyy
# Create  

####
import cv
import numpy as np

im = cv2.imread("checkerboardSmall.png",0) # Grayscale image
Ix = np.zeros(
# a = i and b = j( when looking at the Harris Corner coding notes on gradient
PixelGrad_Array = [] # create an array to store the gradient values from every pixel
SumIxIx = [] #These are the values of all of the IxIx values that are to be summed up
SumIyIy = []
SumIxIy =  []
for i in im:
    for j in im:
        Ix(i,j) = im(i+1,j) - im(i-1,j) # gradient x

        Iy(i,j) = im(i,j+1) -= im(i,j-1) #gradient y

        IxIx = Ix(i,j) *  Ix(i,j)
        SumIxIx.append(IxIx)

        IyIy = Iy(i,j) * Iy(i,j)
        SumIyIy.append(IyIy)

        IxIy = Ix(i,j) * Iy(i,j)
        SumIxIy.append(IxIy)
newMat = [[SumIxIx],[SumIxIy],[SumIxIy],[SumIyIy]]    

Grad_sum  = sum(PixelGrad_Array)

##Kareem Tiwari
##HarrisCorners


####
# Create empty images that are the same size as the original image
# Create Ix, Iy,Ixx,Iyy
# Create  

####
import cv2
import numpy as np

im = cv2.imread("cityscape.jpeg",0) # Grayscale image
numRows = im.shape[0] # x value
numCols  = im.shape[1] # y value
emptyim_Ix = np.zeros((numRows,numCols,1),np.float32)#create  an empty image
emptyim_IxIx = np.zeros((numRows,numCols,1),np.float32)#create  an empty image
emptyim_Iy = np.zeros((numRows,numCols,1),np.float32)#create  an empty image
emptyim_IyIy = np.zeros((numRows,numCols,1),np.float32)#create  an empty image
emptyim_IxIy = np.zeros((numRows,numCols,1),np.float32)#create  an empty image
cornerness_im =  np.zeros((numRows,numCols,1),np.float32)
width = numRows/5
height =  numCols/5

# a = i and b = j( when looking at the Harris Corner coding notes on gradient
PixelGrad_Array = [] # create an array to store the gradient values from every pixel
for i in range(1,numRows-1):
    for j in range(1,numCols-1):
        emptyim_Ix[i,j] = int(im[i+1,j]) - int(im[i-1,j]) # gradient x

        emptyim_Iy[i,j] = int(im[i,j+1]) - int(im[i,j-1]) #gradient y

        emptyim_IxIx[i,j]= emptyim_Ix[i,j] *  emptyim_Ix[i,j]
        
        emptyim_IyIy[i,j] = emptyim_Iy[i,j] * emptyim_Iy[i,j]

        emptyim_IxIy[i,j] = emptyim_Ix[i,j] * emptyim_Iy[i,j]
Max_C=0
for  i  in range(1,numRows-1):
    for j in range(1,numCols-1):
        Sum_IxIx = emptyim_IxIx[i,j]+emptyim_IxIx[i+1,j] +emptyim_IxIx[i-1,j] + emptyim_IxIx[i,j-1] +emptyim_IxIx[i,j+1] +emptyim_IxIx[i-1,j-1]+ emptyim_IxIx[i+1,j+1]+emptyim_IxIx[i-1,j+1] +emptyim_IxIx[i+1,j-1] # These sum up all of the values in the  neighborhood
        Sum_IxIy = emptyim_IxIy[i,j]+emptyim_IxIy[i+1,j] +emptyim_IxIy[i-1,j] + emptyim_IxIy[i,j-1] +emptyim_IxIy[i,j+1] +emptyim_IxIy[i-1,j-1]+ emptyim_IxIy[i+1,j+1]+emptyim_IxIy[i-1,j+1] +emptyim_IxIy[i+1,j-1]
        Sum_IyIy = emptyim_IyIy[i,j]+emptyim_IyIy[i+1,j] +emptyim_IyIy[i-1,j] + emptyim_IyIy[i,j-1] +emptyim_IyIy[i,j+1] +emptyim_IyIy[i-1,j-1]+ emptyim_IyIy[i+1,j+1]+emptyim_IyIy[i-1,j+1] +emptyim_IyIy[i+1,j-1]

        M_det = (Sum_IxIx*Sum_IyIy) -(Sum_IxIy *Sum_IxIy) #This gets the determinant value for every pixel  in the  image
        M_trace = (Sum_IxIx +Sum_IyIy) #This gets the trace value for every pixel in the image
        
        C = M_det - (0.05)*(M_trace)**2
        if C > Max_C:
            Max_C = C
        
        
        cornerness_im[i,j] = C
        
threshold = Max_C*(0.10)
im_color = cv2.imread("cityscape.jpeg") 
for i in range(numRows):
    for j in range(numCols):
        
        if cornerness_im[i,j] > threshold:
            cv2.circle(im_color,(j,i),1,(0,0,255),2)
            

cv2.imshow("new image",im_color)
        
for i in range(5):
    for j in range(5):
        for x  in range((i*int(width)),(i*int(width)+int(width))):
            for y  in range(j*int(height),(j*int(height)+int(height))):

                if cornerness_im[x,y]>threshold:
                    cv2.circle(im_color,(y,x),1,(0,0,255),2)

cv2.imshow("new image2",im_color)
                
        
        
    
        


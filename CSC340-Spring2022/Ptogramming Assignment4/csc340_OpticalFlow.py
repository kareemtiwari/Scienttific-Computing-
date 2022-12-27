##Kareem Tiwari
##Optical Flow


####
# Create empty images that are the same size as the original image
# Create Ix, Iy,Ixx,Iyy
# Create  

####
import cv2
import numpy as np
import math

im = cv2.imread("tree1.jpg",0) # Grayscale image
im_2 = cv2.imread("tree2.jpg",0) # image 2
numRows = im.shape[0] # x value
numCols  = im.shape[1] # y value
emptyim_Ix = np.zeros((numRows,numCols,1),np.float32)#create  an empty image
emptyim_IxIx = np.zeros((numRows,numCols,1),np.float32)#create  an empty image
emptyim_Iy = np.zeros((numRows,numCols,1),np.float32)#create  an empty image
emptyim_IyIy = np.zeros((numRows,numCols,1),np.float32)#create  an empty image
emptyim_IxIy = np.zeros((numRows,numCols,1),np.float32)#create  an empty image
emptyim_It = np.zeros((numRows,numCols,1),np.float32)
emptyim_IxIt = np.zeros((numRows,numCols,1),np.float32)
emptyim_IyIt = np.zeros((numRows,numCols,1),np.float32)
cornerness_im =  np.zeros((numRows,numCols,1),np.float32)
emptyim_u =  np.zeros((numRows,numCols,1),np.float32)
emptyim_v =  np.zeros((numRows,numCols,1),np.float32)
emptyim_mag =  np.zeros((numRows,numCols,1),np.float32)
emptyim_arrow = np.zeros((numRows,numCols,3),np.float32)
emptyim_rgb = np.zeros((numRows,numCols,3),np.float32)
width = numRows/5
height =  numCols/5
count = 0

# a = i and b = j( when looking at the Harris Corner coding notes on gradient
PixelGrad_Array = [] # create an array to store the gradient values from every pixel
for i in range(1,numRows-1):
    for j in range(1,numCols-1):
        emptyim_Iy[i,j] = int(im[i+1,j]) - int(im[i-1,j]) # gradient x

        emptyim_Ix[i,j] = int(im[i,j+1]) - int(im[i,j-1]) #gradient y

        emptyim_It[i,j] = int(im_2[i,j]) - int(im[i,j]) # t value / differnece in the values through images(time)

        emptyim_IxIx[i,j]= emptyim_Ix[i,j] *  emptyim_Ix[i,j]
        
        emptyim_IyIy[i,j] = emptyim_Iy[i,j] * emptyim_Iy[i,j]

        emptyim_IxIy[i,j] = emptyim_Ix[i,j] * emptyim_Iy[i,j]

        emptyim_IxIt[i,j] = emptyim_Ix[i,j] * emptyim_It[i,j]

        emptyim_IyIt[i,j] = emptyim_Iy[i,j] * emptyim_It[i,j]

       
Max_C=0
for  i  in range(6,numRows-5):
    for j in range(6,numCols-5):
        Sum_IxIx = 0
        Sum_IxIy = 0
        Sum_IyIy = 0
        Sum_IyIt = 0
        Sum_IxIt = 0
        for a in range(-5,5):
            for b in range(-5,5):
                 Sum_IxIx += emptyim_IxIx[i+a,j+b]
                 Sum_IxIy += emptyim_IxIy[i+a,j+b]
                 Sum_IyIy += emptyim_IyIy[i+a,j+b]
                 Sum_IyIt += emptyim_IyIt[i+a,j+b]
                 Sum_IxIt += emptyim_IxIt[i+a,j+b]
        
##        Sum_IxIx = emptyim_IxIx[i,j]+emptyim_IxIx[i+1,j] +emptyim_IxIx[i-1,j] + emptyim_IxIx[i,j-1] +emptyim_IxIx[i,j+1] +emptyim_IxIx[i-1,j-1]+ emptyim_IxIx[i+1,j+1]+emptyim_IxIx[i-1,j+1] +emptyim_IxIx[i+1,j-1] # These sum up all of the values in the  neighborhood
##        Sum_IxIy = emptyim_IxIy[i,j]+emptyim_IxIy[i+1,j] +emptyim_IxIy[i-1,j] + emptyim_IxIy[i,j-1] +emptyim_IxIy[i,j+1] +emptyim_IxIy[i-1,j-1]+ emptyim_IxIy[i+1,j+1]+emptyim_IxIy[i-1,j+1] +emptyim_IxIy[i+1,j-1]
##        Sum_IyIy = emptyim_IyIy[i,j]+emptyim_IyIy[i+1,j] +emptyim_IyIy[i-1,j] + emptyim_IyIy[i,j-1] +emptyim_IyIy[i,j+1] +emptyim_IyIy[i-1,j-1]+ emptyim_IyIy[i+1,j+1]+emptyim_IyIy[i-1,j+1] +emptyim_IyIy[i+1,j-1]
##        Sum_IyIt = emptyim_IyIt[i,j]+emptyim_IyIt[i+1,j] +emptyim_IyIt[i-1,j] + emptyim_IyIt[i,j-1] +emptyim_IyIt[i,j+1] +emptyim_IyIt[i-1,j-1]+ emptyim_IyIt[i+1,j+1]+emptyim_IyIt[i-1,j+1] +emptyim_IyIt[i+1,j-1]
##        Sum_IxIt = emptyim_IxIt[i,j]+emptyim_IxIt[i+1,j] +emptyim_IxIt[i-1,j] + emptyim_IxIt[i,j-1] +emptyim_IxIt[i,j+1] +emptyim_IxIt[i-1,j-1]+ emptyim_IxIt[i+1,j+1]+emptyim_IxIt[i-1,j+1] +emptyim_IxIt[i+1,j-1]

    
##        Sum_IxIx = emptyim_IxIx[i+a,j+b]
        
         

        M_det = (Sum_IxIx*Sum_IyIy) -(Sum_IxIy *Sum_IxIy) #This gets the determinant value for every pixel  in the  image
        M_trace = (Sum_IxIx +Sum_IyIy) #This gets the trace value for every pixel in the image
        
        

        if M_det != 0:
            u = ((-Sum_IyIy*Sum_IxIt)+(Sum_IxIy *Sum_IyIt))/(M_det)
            v = ((Sum_IxIy*Sum_IxIt)-(Sum_IxIx*Sum_IyIt))/(M_det)

            emptyim_u[i,j] = u
            emptyim_v[i,j] = v
            

   
##        np.seterr(invalid='ignore')

            
##        Visualization
            mag = math.sqrt((u**2)+(v**2))
            theta  = math.atan2(v,u)
            b_cv = (255*((theta+math.pi)/(2*math.pi)))
            g_CV = (255-b_cv)

            emptyim_mag[i,j] = mag

            

            emptyim_rgb[i,j,0] =  b_cv *mag
            emptyim_rgb[i,j,1] = g_CV *mag
            
            count+= 1
            if count == 35:
                
                cv2.arrowedLine(emptyim_arrow , (int(j), int(i)), (int(j+u), int(i+v)), (b_cv, g_CV, 0))
                count = 0

            




cv2.imshow("image_It",emptyim_It)
cv2.imshow("image_u",emptyim_u) #  this gives me the flow y image
cv2.imshow("image_v",emptyim_v)# this gives me the flow x image
cv2.imshow("image_mag",emptyim_mag)
cv2.imshow("image_color",emptyim_rgb/255)
##cv2.imshow("image_RGB",emptyim_rgb)

##cv2.arrowedLine(emptyim_arrow , (int(j), int(i)), (int(j+u), int(i+v)), (b_cv, 
##g_CV,0))
cv2.imshow("arrows",emptyim_arrow/255)

        
##  Visualizatioon
##
##theta  = math.atan2(v,u)
##b_cv = 255*((theta+math.pi)/(2*math.pi))
##g_CV = ((b_cv -255)/(0-255))



    
        


import numpy as np
import cv2
from matplotlib import pyplot as plt
import random
import math

img1 = cv2.imread('mountainLeft.jpg') # queryImage
img2 = cv2.imread('mountainRight.jpg') # trainImage

im2_Rows = img2.shape[0]
im2_cols = img2.shape[1]

img1_Rows = img1.shape[0]
img1_Cols = img1.shape[1]

# Initiate SIFT detector
sift = cv2.SIFT_create()
##sift = cv2.xfeatures2d.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2) #NOTE: 'None' parameter has to be added (not in documentation)

plt.imshow(img3),plt.show()


pts1 = np.zeros((len(good),2), np.float32)
pts2 = np.zeros((len(good),2), np.float32)
for m in range(len(good)):
	pts1[m] = kp1[good[m][0].queryIdx].pt
	pts2[m] = kp2[good[m][0].trainIdx].pt

opencvH, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, 5.0)
print("H matrix estimated by OpenCV (for comparison):\n", opencvH)


##A = []
##best_dist = 300000
##for a in range(0,500):
##    for r in range(4):
##        i = random.randint(0,len(good)-1)
##            
##        qIdx = good[i][0].queryIdx
##        tIdx = good[i][0].trainIdx
##        x1 = kp1[qIdx].pt[0]
##        y1 = kp1[qIdx].pt[1]
##        x2 = kp2[tIdx].pt[0]
##        y2 = kp2[tIdx].pt[1]
##
##        A.append([0,0,0,-x2,-y2,-1,(y1*x2),(y1*y2),-y1])
##        A.append([x2,y2,1,0,0,0,(-x1*x2),(-x1*y2),-x1])
##
##
##    U, s, V = np.linalg.svd(A, full_matrices=True)
##    hCol = np.zeros((9,1), np.float64)
##    hCol = V[8,:]
##
####print("MyMatrix",hCol/hCol[8])
##    H = [[hCol[0],hCol[1],hCol[2]],[hCol[3],hCol[4],hCol[5]],[hCol[6],hCol[7],hCol[8]]]
##    distance_sum = 0
##    for i in range(len(good)):
##                
##        qIdx = good[i][0].queryIdx
##        tIdx = good[i][0].trainIdx
##        x1 = kp1[qIdx].pt[0]
##        y1 = kp1[qIdx].pt[1]
##        x2 = kp2[tIdx].pt[0]
##        y2 = kp2[tIdx].pt[1]
##
##        kp_1=[x1,y1,1]
##        mp1 = np.dot(H,kp_1) #matrix mult here
##            
##        mp1 = mp1/mp1[2]
##        distance1 = math.sqrt(((mp1[0]-x2)**2)+((mp1[1]-y2)**2))
##        distance_sum = distance1 + distance_sum
##
##        if distance_sum < best_dist:
##            best_dist = distance_sum
##            best_H = H
##
##print("This is my best H: ",best_H)


mapped_corners = []
corners= ([0,0,1],[img1.shape[1],0,1],[0,img1.shape[0],1],[img1.shape[1],img1.shape[0],1])
min_x = 0
max_x = 0
min_y = 0
max_y = 0
all_y = []
all_x = []

for r in range(4):
    new_H =  np.dot(opencvH,corners[r])
    mapped_corners.append(new_H/new_H[2])


for i in mapped_corners:
    all_x.append(i[0])
    all_y.append(i[1])

for i in corners:
    all_x.append(i[0])
    all_y.append(i[1])


min_x = min(all_x)
max_x = max(all_x)
min_y = min(all_y)
max_y = max(all_y)

p_cols =  (int(max_x) - int(min_x)) 
p_rows = int(max_y) - int(min_y)

        
##print(all_x)
##print(all_y)


pano = np.zeros((p_rows,p_cols,3), np.float32)

plt.imshow(pano),plt.show()


for i in range(im2_Rows):
    for j in range(im2_cols):

        pano[i+int(abs(min_y))][j+int(abs(min_x))][0] = img2[i][j][0]
        pano[i+int(abs(min_y))][j+int(abs(min_x))][1] = img2[i][j][1]
        pano[i+int(abs(min_y))][j+int(abs(min_x))][2] = img2[i][j][1]

print(p_rows)
print(p_cols)
Hinv = np.linalg.inv(opencvH)

for i in range(p_rows): # iterate over the height of the image, y-coordinates
    for j in range(p_cols): # iterate over the width of the image, x-coordinates
        
        pt1 = [j-int(abs(min_x)),i-int(abs(min_y)),1]
        pt2 =  np.dot(Hinv,pt1)
        pt2 = pt2/pt2[2]

        if pt2[0] > 0 and pt2[0] < img1_Cols:
            if pt2[1] > 0 and pt2[1] < img1_Rows:

                pano[i,j] = img1[int(pt2[1]),int(pt2[0])]
            
        
        
##
        #access va;ues at pixel:
##        pano[i][j][0] = img1[int(pt2)] # blue value stored at pixel(i,j)
##        k +=1
##        pano[i][j][1] = img1[int(pt2)] # green value stored at pixel(i,j)
##        k +=1                    
##        pano[i][j][2] = img1[int(pt2)]# red value stored at pixel(i,j)

        





cv2.imshow("Pano",pano/255)




# Extra Syntax
######## Get coordinates for the ith match
##        qIdx = good[i][0].queryIdx
##        tIdx = good[i][0].trainIdx
##        x1 = kp1[qIdx].pt[0]
##        y1 = kp1[qIdx].pt[1]
##        x2 = kp2[tIdx].pt[0]
##        y2 = kp2[tIdx].pt[1]


###### Run SVD
##    U, s, V = np.linalg.svd(a, full_matrices=True)
##    hCol = np.zeros((9,1), np.float64)
##    hCol = V[8,:]


###### Invert matrix
##    Hinv = np.linalg.inv(H)


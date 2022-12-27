import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('waterfall1.jpg',0) # queryImage
img2 = cv2.imread('waterfall2.jpg',0) # trainImage

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

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


#RANSAC LOOP



# Extra Syntax
###### Get coordinates for the ith match
##        qIdx = good[i][0].queryIdx
##        tIdx = good[i][0].trainIdx
##        x1 = kp1[qIdx].pt[0]
##        y1 = kp1[qIdx].pt[1]
##        x2 = kp2[tIdx].pt[0]
##        y2 = kp2[tIdx].pt[1]


###### Run SVD
##    U, s, V = np.linalg.svd(A, full_matrices=True)
##    hCol = np.zeros((9,1), np.float64)
##    hCol = V[8,:]


###### Invert matrix
##    Hinv = np.linalg.inv(H)



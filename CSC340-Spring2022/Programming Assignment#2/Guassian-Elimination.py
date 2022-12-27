# CSC 340
# Programmig assignmnet #3

# Kareem Tiwari

##
## create an augmented matrix
##Mat = [[9, -4], [2],
##       [-3], [0], [6],
##       [3], [1], [3]]
##Mat =[[9,-4,2],[-3,0,6],[3,1,3]]
##Mat = [[1,0,0,0,-3],[1,1,1,1,0],[1,2,4,8,5],[1,3,9,27,18]]
##Mat = [[1,0,2, 1],[2,-1,3,-1],[4,1,8,2]]
Mat = [[1,-1,0],[-2,2,-1],[0,1,-2]]
E=1

print(Mat)

for j in range(len(Mat)): # itterate throught the columns in the matrix
    maxVal = 0
    maxPos = 0
    for i in range(j,len(Mat)): # 
       if abs(Mat[i][j]) > maxVal: #find the max value
           maxVal = abs(Mat[i][j]) 
           maxPos = i
    temp = Mat[maxPos]
    Mat[maxPos] = Mat[j] # swap values
    Mat[j] = temp
    dividend = Mat[j][j] #set the dividend
    
    for a in range(j+1, len(Mat)):
        Mult = Mat[a][j]
        if a != j:

            for i in range(len(Mat[0])):


                Mat[a][i] = (Mat[a][i]) - (Mat[j][i]*Mult/dividend)

print(Mat)
print(Mat[a][i])

####Find largest magnitude in first column
##for i in range(int(Mat[0][0]), int(Mat[8][0])):
##    if abs(Mat[3][0]) > abs(Mat[0][0]) < abs(Mat[6][0]):
##        if abs(Mat[3][0]) < abs(Mat[6][0]):
##            Mat[0][0] = Mat[0][0]
##            Mat[6][0] = Mat[6][0]
##            Mat[3][0] = Mat[3][0]
##
##
##        else:
##            Mat[0][0] = Mat[0][0]
##            Mat[6][0] = Mat[6][0]
##            Mat[3][0] = Mat[3][0]
##
##    else:
##        Mat[0][0] = Mat[0][0]
##        Mat[3][0] = Mat[3][0]
##        Mat[6][0] = Mat[6][0]
##print(Mat)
#### NO SWAPPPP
#### multiply then subtract
###Column 1
##for i in range(int(Mat[0][0]), int(Mat[8][0])):
##    if Mat[3][0] != 0:
##            # row 2
##        Mat[3][0] = Mat[3][0] - ((Mat[3][0]/Mat[0][0]) * Mat[0][0])
##        Mat[4][0] = Mat[4][0] - ((Mat[3][0]/Mat[0][0]) * Mat[1][0])
##        Mat[5][0] = Mat[5][0] - ((Mat[3][0]/Mat[0][0]) * Mat[2][0])
##
##    else:
##        Mat[3][0] = Mat[3][0]
##        Mat[4][0] = Mat[4][0]
##        Mat[5][0] = Mat[5][0]
##for i in range(int(Mat[0][0]), int(Mat[8][0])):
##    if Mat[6][0] != 0:
##        # row 3
##        Mat[6][0] = Mat[6][0] - ((Mat[6][0]) / (Mat[0][0]) * Mat[0][0])
##        Mat[7][0] = Mat[7][0] - ((Mat[6][0]) / (Mat[0][0]) * Mat[1][0])
##        Mat[8][0] = Mat[8][0] - ((Mat[6][0]) / (Mat[0][0]) * Mat[2][0])
##
##    else:
##        Mat[6][0] = Mat[6][0]
##        Mat[7][0] = Mat[7][0]
##        Mat[8][0] = Mat[8][0]
##
##print(Mat)

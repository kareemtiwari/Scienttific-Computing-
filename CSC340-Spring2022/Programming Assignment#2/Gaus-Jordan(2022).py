# CSC 340
# Programmig assignmnet #3

# Kareem Tiwari

##
## create an augmented matrix
##Mat=[[1,-2,0,-4],
##     [3,1,-2,1],
##     [0,-2,2,2]]
##Mat = [[1,0,2, 1],[2,-1,3,-1],[4,1,8,2]]
Mat = [[1,-1,0,1,0,0],
       [2,0,4,0,1,0],
       [0,2,-1,0,0,1]] #Use this one  to show the inverse
##Mat = [[1,0,0,0],[1,1,1,1],[1,2,4,8],[1,3,9,27]]
##print(Mat)
#his  is a parameter to check if the algorithm successfully found a unique solution
#This loop finds the greatest magnitude in column one
#Column one
# this is the swap,multiplication, adn subtraction all for column one
E=1

for j in range(len(Mat)):
    maxVal = 0
    maxPos = 0
    for i in range(j,len(Mat)):
       if abs(Mat[i][j]) > maxVal: # find the max value
           maxVal = abs(Mat[i][j])
           maxPos = i
    temp = Mat[maxPos]  # swap values
    Mat[maxPos] = Mat[j]
    Mat[j] = temp
    dividend = Mat[j][j]  # Divide by the value on the diagonal
    for i in range(len(Mat[0])): 

       Mat[j][i] = Mat[j][i]/(dividend) #divide every value by the value on the diagonal


    for a in range(len(Mat)):
        Mult = Mat[a][j]
        if a != j:

            for i in range(len(Mat[0])):


                Mat[a][i] = Mat[a][i]- (Mat[j][i]*Mult)

print(Mat)


                # if Mat[i][j] == 1:
                    # print("The value on the diagonal is one")
                # else:
                    # print("The value on the diagonal is NOT one, something isn't right")


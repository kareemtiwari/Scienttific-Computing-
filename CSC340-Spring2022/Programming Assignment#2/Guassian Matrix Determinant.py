#Guassian Elimination Matrix Determinant


##Mat = [[1,0,2, 1],[2,-1,3,-1],[4,1,8,2]]
Mat = [[1,-1,0],[-2,2,-1],[0,1,-2]]
r = 0 # counter
E = 1

for j in range(len(Mat)):
     maxVal = 0
     maxPos = 0
     for i in range(j,len(Mat)): #
          if abs(Mat[i][j]) > maxVal: #find the max value
               
               maxVal = abs(Mat[i][j]) 
               maxPos = i
     if maxPos != j:
          temp = Mat[maxPos]
          Mat[maxPos] = Mat[j] # swap values
          Mat[j] = temp
          dividend = Mat[j][j] #set the dividend
          r += 1

     for a in range(j+1, len(Mat)):
        Mult = Mat[a][j]
        if a != j:
             
             Mat_det =  (-1**r)* (Mat[j][i]*Mult/dividend)
print(Mat)
print(Mat_det)
     
    

    
    

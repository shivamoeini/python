# Program to multiply two matrices using nested loops

# ۳x3 matrix
X = [[6,6,1],
    [9,2,4],
    [3,6,5]]
# ۳x4 matrix
Y = [[1,3,6,1],
    [3,4,3,2],
    [7,6,3,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)

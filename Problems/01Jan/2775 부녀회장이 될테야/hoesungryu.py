# make 2d-array 
row = 15
colum = row - 1 
Matrix = [[0 for j in range(14)] for i in range(15)]
for i in range(15):
    Matrix[i][0]=1     
for j in range(14):
    Matrix[0][j]=j+1

for i in range(1,15):
    for j in range(1,14):
	    Matrix[i][j] = Matrix[i][j-1] + Matrix[i-1][j]

# answer 
case = int(input())
for _ in range(case):
    k = int(input())
    n = int(input())
    print(Matrix[k][n-1])

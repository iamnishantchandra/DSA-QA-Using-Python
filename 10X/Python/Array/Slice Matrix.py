'''
Slice Matrix
Given a matrix(2-D array), and 4 numbers left,right,top,bottom(1 based indexing), slice the submatrix(including the margins) out of the matrix .

I.e- slice the submatrix with top <= row number<= bottom and right <= column number<= left

1<=left <= right<=(number of columns) and 1<=top<=bottom<=(number of rows)


Input
first line of the input contains 2 numbers(space separated) representing the number of rows and columns of 
the input matrix(r,c). following 'r' lines represent the 'r' rows of the matrix with each elements separated 
by space. The final line contains 4 numbers representing the left,right,top,bottom margins(1 based indexing) 

respectively, of the submatrix

Output
Print the submatrix(including the margins), with each row being printed in separate line(elements space separated).

Example
Input:

3 4

1 2 3 4

5 6 7 8

9 2 3 1

2 4 1 3

Output:

2 3 4

6 7 8

2 3 1

Explanation

l,r,t,b=2,4,1,3. hence we need to take submatrix from 2nd column to 4th column and 1st row to 3rd row. which is [[2,3,4],[6,7,8],[2,3,1]].
'''
'''
m,n=map(int,input().split())
a=[]
x=0
y=0
for i in range(m):
    b=list(map(int,input().split()))
    a.append(b)
if len(a)==len(a[0]):
    print(len(a))
    print(len(a))
    x=1
    y=1
elif len(a)==len(a[0])-1:
    x=1
    y=0
for i in range(0,len(a)-x):
    for j in range(y,len(a[i])):
        print(a[i][j],end=" ")
    print()
'''
m,n=map(int,input().split())
a=[]
l=0
r=0
t=0
b=0
for i in range(m):
    b=list(map(int,input().split()))
    a.append(b)
l,r,t,b=map(int,input().split())
for i in range(t-1,b):
    for j in range(l-1,r):
        print(a[i][j],end=" ")
    print()

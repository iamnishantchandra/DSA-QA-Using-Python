'''
Pascal Triangle
Pascal’s triangle is a triangular array of the binomial coefficients. Write a function that takes an integer value n as input and prints first n lines of the Pascal’s triangle.

Following is the representation of a pascal triangle of depth 5

1

1 1

1 2 1

1 3 3 1

1 4 6 4 1

Refer to below link for more information

https://en.wikipedia.org/wiki/Pascal%27s_triangle

Input
You will be given N, depth of the traingle

Output
Print pascal triangle cofficients at depth N

Example
Input:

4

Output:

1

3

3

1

At depth 4 the elements are 1 3 3 1.


'''
n=int(input())
a=[]  
for i in range(n):
    a=[]
    if n==0:
        print(0)
        break
    else:
        a.append(11**i)
a=a[0]
while a>0:
    print(a%10)
    a//=10

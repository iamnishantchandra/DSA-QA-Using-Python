'''
Good will
A good will triangle of order n is defined as follows:

Lets say n = 5,

    *
   $*$
  *$*$*
 $*$*$*$
*$*$*$*$*
You have been given a positive integer n, you need to print the good will triangle for the given integer.

Input Format:
One positive integer denoting n.

Output Format:
Print the resultant good will triangle of order n.

Example:
Input:

3
Output:

  *
 $*$
*$*$*
'''
n=int(input())
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j>i:
            print(" ",end="")
        elif j%2==0:
            print("$",end="")
        else:
            print("*",end="")
    for j in range(1,i):
        if j%2==0:
            print("*",end="")
        else:
            print("$",end="")
    print()           
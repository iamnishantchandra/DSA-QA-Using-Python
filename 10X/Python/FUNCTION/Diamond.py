'''
Diamond
Given n, print the pattern like this: (For example, if n=5)

    * 
   ***
  ***** 
 ******* 
********* 
 *******
  *****
   ***
    * 
Input
One Integer, denoting n.

Output
Print the desired pattern.

Example
Input1:

3
Output1:

  *
 ***
*****
 ***
  *

'''
n=int(input())
for i in range(1,n+1):
    print(((" ")*(n-i))+(("*")*(i)),end="")
    
    print((("*")*(i-1))+((" ")*(n-i)),end="")
    print()
for j in range(1,n):
    print(((" ")*(j))+(("*")*(n-j)),end="")
    
    print((("*")*(n-j-1))+((" ")*(j)),end="")
    print()
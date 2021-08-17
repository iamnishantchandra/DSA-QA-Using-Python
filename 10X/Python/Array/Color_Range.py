'''
Color Sort
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Solve this problem without using the library's sort function
Come up with a one-pass algorithm using only O(1) constant space
Input
First line denotes n, the size of the array nums. The next n lines contains elements of the array nums.

Output
n lines denoting the elements of the resultant array.

Example
Input:

6
2
0
2
1
1
0
Output:

0
0
1
1
2
2
Constraints:
n == nums.length
1 <= n <= 1000000
nums[i] is 0, 1, or 2.
'''
"""
n=int(input())
a=[]
while n>0:
    b=int(input())
    if b==0:
        a.insert(0,0)
    elif b==2:
        a.append(2)
    elif b==1:
        '''for j in range(len(a)):
            if a[j]==1:'''
            
""" 
"""
elif b==2:
        a.append(2)
elif b==1:
        a.insert(count,1) 
----------------------------------
n=int(input())
a=[]
count=0
for i in range(n):
    b=int(input())
for i in a:
    if i==0 and b==0:
        a.append(b)
    elif i==1 and b==1:
        a.append(b)
    elif i==2 and b==2:
        a.append(b)

for k in a:
    print(k)
"""
n=int(input())
a=[]
Red=0
white=0
Blue=0
for i in range(n):
    b=int(input())
    if b==0:
        Red+=1
    elif b==1:
        white+=1
    elif b==2:
        Blue+=1
for i in range(Red):
    print(0)
for i in range(white):
    print(1)
for i in range(Blue):
    print(2)
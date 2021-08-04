'''
Zebra
You have been given n non-negative integer values. Lets say the given values are a1, a2, a3, a4 ...

You need to find out whether these values can form a zebra crossing or not (in the same order).

Note that in zebra crossing, there are alternate white colors (denoted as positive numbers here), and 
empty or black colors (denoted by non-positive numbers here).

Input Format:
First line denotes n, the number of inputs. The next n lines contains one integer in each line.

Output Format:
One value denoting True or False.

Example:
Input:

5
10
20
30
40
50
Output:

False


'''
"""
n=int(input())
l = []
f=False
for i in range(0,n):
    l.append(int(input()))

for i in range(0,n-1):
    if (l[i]>0 and l[i+1]<0):
        f=True
    elif l[i]<0 and l[i+1]>0:
        f=True
    else:
        f=False
        print(f)
        break
if f:
    print(True)

'''elif (prev<0 and c>0):
        f=True'''
"""
n=int(input())
f=False
prev=int(input())
for i in range(0,n-1):
    c=int(input())
    if (prev>0 and c<0)or(prev<0 and c>0):
        f=True
    else:
        f=False
        print(f)
        break
    prev=c
if f:
    print(True)




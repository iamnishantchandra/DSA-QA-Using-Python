'''
Pattern122333
Write a program to make such a pattern like right angle triangle with a number which will repeat a number in a row, as shown below.

For n = 4, the pattern should be like:

1
22
333
4444
Input
One Integer, denoting n.

Output
The required pattern

Example
Input1:

5
Output1:

1
22
333
4444
55555

'''
n=int(input())
a=0
for i in range(1,n+1):
    for j in range(0,i):
        print(i,end="")
    print()






'''
Reduce Array
link-  https://6793fdf6.widgets.sphere-engine.com/lp?hash=89o7WLgUCl

You are given a list of integers. Your task is to reduce the list to a single integer. Following are 
the rules to do this reduction:

[ADD] Sum first two numbers and result is m
[SUB] Say third number is e3, subtract e3 from this: m-e3
[ADD] Say fourth number is e4, add to previous result: m-e3+e4
[SUB] Subtract next number from the previous result
[ADD] Add next number to previous result and so on
until you reach the end of the list
the result at this point is the output of the problem
Input
First line is n, 1 <= n <= 100, denoting the number of elements in the list

This is followed by n lines, one integer on each line

Output
One integer indicating the output

Example
Input:

5

1

2

-1

5

10

Output:

-1

Explanation
First line is 5, indicating 5 elements in the list

The 5 elements follow in the next 5 lines: 1,2,-1,5,10

First add, 1+2=3

Next subtract, 3-(-1)=4

Next add, 4+5=9

Next subtract, 9-10=-1

No more elements, result is -1

'''
import array
n=int(input())
a=array.array('i',[])
for i in range(n):
    a.append(int(input()))
m=a[0]
for i in range(1,n):
    if i%2!=0:
        m+=a[i]
    else:
        m-=a[i]
print(m)
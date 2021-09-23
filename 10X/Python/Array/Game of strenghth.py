'''
Game of Strength
Andrew is very fond of Maths.He has N boxes with him,in each box there is some value which represents the 
Strength of the Box.The ith box has strength A[i]. He wants to calculate the Overall Power of the all N 
Boxes.

Overall Power here means Sum of Absolute Difference of the strengths of the boxes(between each pair of 
boxes) multiplied by the Maximum strength among N boxes. Since the Overall Power could be a very large 
number,output the number modulus 10^9+7(1000000007).

Input
First line of the input contains the number of test cases T. It is followed by T test cases. Each test 
case has 2 lines. First line contains the number of boxes N. It is followed by a line containing N elements 
where ith element is the strength of Andrew's ith box.

Output
For each test case, output a single number, which is the Overall Power for that testcase.

Example
Input:

2

2

1 2

5

4 5 3 1 2

Output:

2

100

'''
for _ in range(int(input())):
    n=int(input())
    arr=[int(x) for x in input().split()]
    su=0
    f=0
    suarr=sum(arr)
    ma=max(arr)
    for i in range(len(arr)):
        su+=abs((arr[i]*len(arr))-suarr)
    f=su*ma
    print(su)
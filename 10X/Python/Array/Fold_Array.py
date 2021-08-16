'''
Fold Array

link   https://6793fdf6.widgets.sphere-engine.com/lp?hash=ZgW2gfNUI6

You are given an array of size n, 0 <= n <= 100. Imagine the array as a length of rope. You have to fold 
the rope at the middle. You are also given an input integer num_folds that specifies the number of times 
you should fold your array.

To illustrate more, say the given array is 1,4,9. Folding it in the middle results in 10, 4 as 9 and 1 
get combined by the fold.

Say the given array is 1,10,20,21,2. Folding it would lead to: 3, 31, 20 as 2, 1 have combined and 10, 
21 have combined.

Based on the num_folds repeat folding.

Input.
The first line contains n, the number of elements in the array. 0 <= n <= 200

This is followed by n lines, each containing one integer

The last line contains m, the number of folds to do. 0 <= m <= 6

Output
The first line contains k, the number of elements in the final array

This is followed by k lines, each containing one integer element of the output array

Example
Odd length array
Input:

5

-1

4

2

3

1

1

Output:

3

0

7

2

Even length array
Input:

6

3

1

6

7

2

3

1

Output:

3

6

3

13

Explanation
Odd number n
The first line contains 5 indicating 5 elements in the input array

The next 5 lines contain the array elements: -1, 4, 2, 3, 1

The last line contains 1 indicating one fold to be made

The first and last element merge: -1 + 1 = 0

The second and 4th element merge: 4 + 3 = 7

The middle element is 2. It remains unchanged because of the fold

So the result is 0, 7, 2

Even number n
The first line contains 6 indicating 6 elements in the input array

The next 6 lines contain the array elements: 3, 1, 6, 7, 2, 3

The last line contains 1 indicating one fold to be made

The first and last element merge: 3 + 3 = 6

The second and 5th element merge: 1 + 2 = 3

The third and 4th element merge: 6 + 7 = 13

So the result is 6, 3, 13
'''
'''
import array
n1=int(input())
a=array.array('i',[])

for i in range(n1):
    a.append(int(input()))
fold=int(input())
for j in range(fold):
    n=len(a)
    if n%2==0:
        for i in range(n//2):
            a[i]=a[i]+a[(n-i)-1]
            a=a[0:(n//2+1)]
    elif n%2!=0:
        for i in range(n//2+1):
            a[i]=a[i]+a[(n-i)-1]
            a=a[0:(n//2+1)]
print(a)
'''
import array
n1=int(input())
a=array.array('i',[])

for i in range(n1):
    a.append(int(input()))
fold=int(input())
if (0 <= n1 <= 200) and (0 <= fold <= 6):
    for j in range(fold):
        b=array.array('i',[])
        n=len(a)
        if n%2==0:
            for i in range(n//2):
                b.append(a[i]+a[n-i-1])
        elif n%2!=0:
            for i in range(n//2):
                b.append(a[i]+a[n-i-1])
            b.append(a[(n//2)])
        a=b
    print(len(a))
    for i in a:
        print(i)


    
'''
Matrix Diagonal
Write a function which takes a 2 dimentional array of size nxn where n > 0 and changes its diagonal according to the following conditions

if an element e < 0 replace it with 0
If element e >= 0 replace it with 1
Input
The first line contains n, denoting the number of lists.

This is followed by n lines. Each line contains n integers separated by a space

Output
n lines, each line representing a list of numbers separated by a space.

Example
Input:

4

2 0 1 4

0 -1 1 10

0 0 0 0

1 2 3 4

Output:

1 0 1 4

0 0 1 10

0 0 1 0

1 2 3 1
'''
# name your function as change_diagonal and it should take list as input
def change_diagonal(lst):
    for i in range(val):
        for j in range(val):
            if i==j:
                if lst[i][j]<0:
                    lst[i][j]=0
                elif lst[i][j]>=0:
                    lst[i][j]=1
    return lst




# Do not change anything below this line.
if __name__ == "__main__":
    val = int(input())
    lst = []
    for index in range(0, val):
        lst.append([int(i) for i in input().split(' ')])
    out = change_diagonal(lst)
    for lst1 in out:
        print(" ".join(str(i) for i in lst1))
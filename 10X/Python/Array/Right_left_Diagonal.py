'''
Right to Left Diagonal
Write a function right_to_left_diagonal which a matrix as a list of lists of size mxm and returns a list of numbers containing elements of diagonal from right to left.

Input
M size of matrix

M lines containing M elements in each line separated by space

Output
list of m elements 1 per each line.

Example
Input: 4

1 2 3 4

5 6 7 8

9 10 11 12

13 14 15 16

Output:

4

7

10

13

'''
# name your function as right_to_left_diagonal
def right_to_left_diagonal(lst):
    out=[]
    for i in range(m):
        for j in range(m):
            if (m-1)==j+i:
                out.append(lst[i][j])
    return out

# Do not change anything below this line
if __name__ == "__main__":
    m = int(input())
    lst = []    
    for val in range(0, m):
        lst.append([int(i) for i in input().split(' ')])
    out = right_to_left_diagonal(lst)
    [print(val) for val in out]
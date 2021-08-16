'''
Rotate Matrix
You are given m lists. Each list contains n elements. Represented as a matrix, this has m rows and n columns. Your task is to rotate clockwise around the center and output the result.

Matrix rotation example 1
Given a matrix:

 a b c d

 e f g h
the rotation is:

 e a 
 f b 
 g c 
 h d 
Matrix rotation example 2
Given a matrix:

 a b c
 d e f
 g h i
the rotation is:

 g d a
 h e b
 i f c
Input
The first line contains m, denoting the number of lists

This is followed by m lines each containing n integers separated by space

Output
The first line should contain the number of rows in the output matrix, say p

The next p lines should contain each row of the matrix, with the elements separated by a space

Example
Input:

3

1 2 3 4

5 6 7 8

9 10 11 12

Output:

4

9 5 1

10 6 2

11 7 3

12 8 4

Explanation
The first line in the input contains 3 indicating that there are 3 rows in the matrix.

The next 3 lines contain each row of the matrix

The given matrix transpose has 4 rows. The first line of the output is 4

This is followed by 4 lines, each containing one row of the output matrix
'''
def transpose_matrix(lst):
    arr=[]

    for j in range(len(lst[0])):
        ar=[]
        for i in range(len(lst)):
            ar.append(lst[(len(lst))-i-1][j])
        arr.append(ar)
    print(len(arr))
    return arr



# do not change anything below this line
if __name__ == "__main__":
    h = int(input())
    lst = []
    for val in range(0, h):
        lst.append([int(i) for i in input().split(' ')])

    out = transpose_matrix(lst)
    for val in out:
        print(" ".join(str(i) for i in val))
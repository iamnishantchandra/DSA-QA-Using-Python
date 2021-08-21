'''
Sum of Diagonals
Description
Given a square matrix, print the sum of all the numbers on both the diagonals.

Input format
First line contains a positive integer n, denoting the number of rows and columns It is followed by n 
lines. Each line contains space separated integers denoting elements of that row.

Output format
One line containing the sum of all the numbers on both the diagonals.

Sample input
3
1 2 3
4 5 6
7 8 9
Sample output
30
Explanation
First line is 3, i.e. 3 rows and 3 columns. We can see that there are 2 diagonals [1,5,9] and [3,5,7]. 
When we add all the numbers in both the diagonals, it comes up to 15 + 15 which is 30 which is our output


'''
# name your function as change_diagonal and it should take list as input
def change_diagonal(lst):
    sum1=0
    sum2=0
    for i in range(val):
        for j in range(val):
            if i==j:
                sum1+=lst[i][j]
            if (val-1)==j+i:
                sum2+=lst[i][j]
    return sum1+sum2



# Do not change anything below this line.
if __name__ == "__main__":
    val = int(input())
    lst = []
    for index in range(0, val):
        lst.append([int(i) for i in input().split(' ')])

    print(change_diagonal(lst))
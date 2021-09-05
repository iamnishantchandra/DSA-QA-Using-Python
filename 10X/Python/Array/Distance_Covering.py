'''
Distance covering
Description
Given a distance n, find the number of ways to cover it with either 1 or 2 steps.

Input format
First line contains a positive integer n, the number of test cases.
This is followed by n lines, each line containing an integer p, 1 <= p <= 20.

Output format
n lines, each line containing a positive integer, denoting the number of ways to cover the corresponding distance.

Sample input
2
3
2
Sample output
3
2
Explanation
First line of input is 2, meaning there are 2 test cases.
Next line contains 3, indicating that the distance to be covered is 3 units.
We can cover a distance of 3 in the following ways:

Path 1: 1-1-1
Path 2: 1-2
Path 3: 2-1
So, the first line of output is 3.
Next line contains 2, indicating that the distance to be covered is 3 units.
We can cover a distance of 2 in the following ways:

Path 1: 1-1
Path 2: 2
So, the second line of output is 2.

'''
def dist(n):
    if n<=2:
        return n
    return dist(n-1)+dist(n-2)
for _ in range(int(input())):
    print(dist(int(input())))
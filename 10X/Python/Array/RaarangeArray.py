'''
Rearrange Array
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

Input
First line of the input denotes n, the size of the given arrays. The next n lines denotes the elements of 
the nums array and the next n elements denotes the elements of the index array.

Output
n lines, each containing a single element from the resultant array.

Example
Input:

5
0
1
2
3
4
0
1
2
2
1
Output:

0
4
1
3
2
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]

'''
n=int(input())
nums=[]
ind=[]
target=[]
for i in range(n):
    nums.append(int(input()))
for i in range(n):
    ind.append(int(input()))
for i in range(n):
    target.insert(ind[i],nums[i])
[print(target[i]) for i in range(n)]
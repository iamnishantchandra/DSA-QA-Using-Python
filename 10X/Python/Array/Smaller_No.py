""""
Smaller Numbers
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Input
First line consists of a single integer, denoting N, length of array.

Next N lines containing one integer per line denoting the elements of array A.

Output
Print the resultant array, one element in one line.

Constraints:
2 <= nums.length <= 500
0 <= nums[i] <= 100
Example
Input:

5

8

1

2

2

3

Output:

4

0

1

1

3

Explanation
nums = [8,1,2,2,3]

Output: [4,0,1,1,3]

For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).

For nums[1]=1 does not exist any smaller number than it.

For nums[2]=2 there exist one smaller number than it (1).

For nums[3]=2 there exist one smaller number than it (1).

For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
"""
"""
a=[int(input())for x in range(int(input())) ]
inlis=[]
outlis=[]
no=a[0]
inlis.append(no)
for i in range(1,len(a)):
    if a[i]<a[0]:
        inlis.append(a[i])

for j in range(len(inlis)):
    count=0
    for i in range(len(a)):
        if inlis[j]>a[i]:
            count+=1
    outlis.append(count)

#[print(i) for i in outlis] print(outlis)
#print(inlis)
"""
a=[int(input())for x in range(int(input())) ]
b=sorted(a)
for i in a:
    print(b.index(i))
'''
Intersection Sorted Array
Given 2 sorted arrays (Sorted in ascending order). You have to print out the numbers which are in intersection of these 2 arrays. Print -1 if there is intersection is empty.

Input
First line is n which denotes the number of elements in first array. Following n lines are elements for the first array.
Next line is m which denotes the number of elements in second array. Following m lines are elements for the second array.

Output
k lines representing the numbers which are common to both the arrays.

Example
Input:

4
1
1
2
2
3
2
2
5
Output:

2
2
Explanation
First line is 4, i.e. 4 elements in the first array. So the first array is [1,1,2,2].
m is 3, so the second array is [2,2,5].
Comparing the 2 arrays, common elements to both of them are [2,2] which is our output.

'''
'''
def intersect(nums1, nums2):
    # implement this function
    n1={}
    n2={}
    arr=[]
    for i in nums1:
        if i in n1:
            n1[i]+=1
        else:
            n1[i]=1
    for i in nums2:
        if i in n2:
            n2[i]+=1
        else:
            n2[i]=1
    for i in n1:
        if i in n1 and i in n2:
            for j in range(min(n1[i],n2[i])):
               arr.append(i)
    if arr:
        return arr
    else:
        return[-1]



'''
from collections import defaultdict
def intersect(nums1, nums2):
    # implement this function
    n1=defaultdict(int)
    n2=defaultdict(int)
    arr=[]
    n3=defaultdict(int)
    for i in nums1:
        if i in n1:
            n1[i]+=1
        else:
            n1[i]=1
    for i in nums2:
        if i in n2:
            n2[i]+=1
        else:
            n2[i]=1
    for i in n1:
        if i in n1 and i in n2:
            for j in range(min(n1[i],n2[i])):
               arr.append(i)
    if arr:
        return arr
    else:
        return[-1]




# DO NOT change anything below this line
if __name__ == "__main__":
    num1_len = int(input())
    nums1 = []
    for index in range(num1_len):
        nums1.append(int(input()))
    num2_len = int(input())
    nums2 = []
    for index in range(num2_len):
        nums2.append(int(input()))

    for element in intersect(nums1, nums2):
        print(element)
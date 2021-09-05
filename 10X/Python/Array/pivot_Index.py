'''
Pivot Index
Description
Given an array of n integers. Write a method that returns the "pivot" index of this array. We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index. If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
Please assume that the sum to the left of the first element and the right of the last element is 0, i.e Sum of numbers which are not in bounds of the given array is 0

Input format
First line contains a positive integer n, denoting the number of elements in the array. Following n lines contain one integer each denoting one element in the array.

Output format
One integer containing the integer of the pivot element.

Sample input
6
1
7
3
6
5
6
Sample output
3
Explanation
First line is 6, i.e. 6 elements in the array.
The actual array is [1,7,3,6,5,6].
If we split the array by the number 6 at index 3, the left side array is [1,7,3] and the right side array is [5,6]
Left side array is of sum 11 and right side array is of sum 11 so the 6 at index 3 is the pivot element so 3 is the output.

Sample input
3
1
2
3
Sample output
-1
Explanation
First line is 3, i.e. 3 elements in the array.
The actual array is [1,2,3].
There is no way that we can split the array such that the sum of left side of the array is equal to the right side of the array.
So the output is -1.
'''
# def pivotIndex(arr):
#     # Implement this function
#     i=0
#     j=0
#     rsum=0
#     lsum=0
#     while i<len(arr)-1 and j<len(arr):
#         j=i+2
#         for k in range(i):
#             rsum+=arr[k]
#         for k in range(j,len(arr)):
#             lsum+=arr[k]
#         if rsum==lsum:
#             return i+1
#         i+=1
#     return -1


# # Do not edit anything below
# if __name__ == "__main__":
#     num_elems = int(input())
#     nums = []
#     for i in range(num_elems):
#         nums.append(int(input()))
        
#     print(pivotIndex(nums))

###########################################
def pivotIndex(arr):
    # Implement this function
    if len(arr)==1:
        return 0
    rsum=arr[0]
    lsum=sum(arr[0:len(arr)])
    for i in range(0,len(arr)-1):
        rsum-=arr[i]
        lsum-=arr[i]
        if lsum==rsum:
            return i
        rsum+=arr[i]
        lsum-=arr[i+1]
    return -1

# Do not edit anything below
if __name__ == "__main__":
    num_elems = int(input())
    nums = []
    for i in range(num_elems):
        nums.append(int(input()))
        
    print(pivotIndex(nums))
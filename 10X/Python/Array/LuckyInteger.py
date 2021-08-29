'''
Lucky Number
Given a sorted array of n integers, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there is no lucky integer return -1.

If you have multiple lucky integers, please return the first lucky integer in the array (lucky number with the least index).

Input
First line contains a positive integer n, denoting the number of elements in the array. It is followed by n lines. Each line contains one integer denoting an element in the array.

Output
One line specifying the lucky integer in the array

Example
Input:

4
2
2
3
4
Output:

2
Explanation
First line is 4, i.e. 4 elements in the array. The array is [2,2,3,4]. We can see that number 2 is repeating 2 times hence it is the lucky number which is our output

'''
'''
def findLuckyNumber(nums):
    for i in range(len(nums)):
        if i==0 and nums[i]==1:
             return nums[i]
        elif nums[i]==i:
            return nums[i]
    return -1
'''
'''
def findLuckyNumber(nums):
    # implement this function
    for i in nums:
        if i==0 and nums[i]==1:
             return nums[i]
        elif count(nums[i])==i:
            return nums[i]
    return -1

# DO NOT change anything below this line
if __name__ == "__main__":
    num_elems = int(input())
    input_arr = []
    for index in range(num_elems):
        input_arr.append(int(input()))
    
    print(findLuckyNumber(input_arr))
'''
def findLuckyNumber(nums):
    # implement this function
    dic={}
    for i in nums:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i in nums:
        if dic[i]==i:
            return i
    return -1



# DO NOT change anything below this line
if __name__ == "__main__":
    num_elems = int(input())
    input_arr = []
    for index in range(num_elems):
        input_arr.append(int(input()))
    
    print(findLuckyNumber(input_arr))
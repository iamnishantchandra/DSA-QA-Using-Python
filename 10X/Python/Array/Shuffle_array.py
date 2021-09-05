'''
Shuffle array
Description
Given an array consisting of 2n elements in the form [x1, x2, ..., xn, y1, y2, ..., yn], suffle the array into [x1, y1, x2, y2, ... , xn, 
yn]. Assume that n is never 0.

Input format
First line contains a positive integer, denoting n. It is followed by 2n lines. Each line contains one 
integer.

Output format
2n lines where each line contains one element of the shuffled array.

Sample input
3
2
5
1
3
4
7
Sample output
2
3
5
4
1
7
Explanation
First line is 3, i.e. Following 6 lines are the elements of the array.
The first 3 lines contains the first half of the array and the 2nd set of 3 elements contain the second 
half of the array.
First 2 lines of output will be first element of first half, first element of second half so the first 2 
lines of the output are 2 and 3.
Next 2 lines of output will be second element of first half and second element of second half, so the 
next 2 lines of output will be 5 and 4
Next 2 lines of output will be third element of first half and third element of second half, so the next 
 lines of output will be 1 and 7
'''
import array
def shuffle(arr):
    # Implement this function
    a=arr
    b=array.array('i',[])
    for i in range(len(a)//2):
            b.append(a[i])
            n=((len(a))//2)+i
            b.append(a[n])
    return b
    '''
    c=a[(len(a)//2):len(a)]
    for i in range(len(c)):
        b.append(a[i])
        b.append(c[i])
    return b            
    '''




# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    nums = []
    for index in range(2 * n):
        nums.append(int(input()))
    for elem in shuffle(nums):
        print(elem)





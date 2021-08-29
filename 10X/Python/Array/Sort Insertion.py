
"""
insertion
The task is to complete the insert() function which is used to implement Insertion Sort. You don't need to worry about input/output.

Insertion Sort Visualization

Input
First line denotes n, the size of the given array. The next line denotes the spaces seperated integers, which are the elements of the given array.

Output
Sorted array, as space seperated values.

Example
Input1:

5
4 1 3 9 7
Output1:

1 3 4 7 9

"""

def insert(arr,n):
    # Your code goes here
    j=0
    for i in range(1,len(arr)):
        j=i
        while(j>0) and arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    return arr
### DO NOT EDIT ANYTHING BELOW THIS LINE

if __name__=='__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    insert(arr, n)
    print(*arr)
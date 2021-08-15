'''
Remove '3'
You have been given an integer as input. you have to remove all the instances of the digit 3 present in the integer and print the remaining integer.

ex- input= 122345337 output= 122457

To solve this problem you have been given a solution template and you need to complete the following functions.

intToArr-> takes integer as input and returns list of all digits of the number.(ex- 123-> [1,2,3])

arrToInt-> takes list of digits as input and returns the corresponding integer to the list.(ex- [1,2,4] -> 124)

remove_3-> takes a list of integers as input and returns a modified list in which every 3 is removed (ex- [1,2,3,4,3]->[1,2,4])

Input
Input contains only 1 integer as input.

Output
print the final integer in which all 3's are removed.

Example
Input:

12353373999983

Output:

125799998
'''
def intToArr(N):
    #complete this function
    temp=0
    n=0
    arr=[]
    while N>0:
        temp=N%10
        N=N//10
        arr.append(temp)
    return arr


def remove_3(arr):
    #complete this function
    ar=[]
    for i in arr:
        if i!=3:
            ar.append(i)
    return ar[::-1]

def arrToInt(arr):
    #complete this function
    sumo=0
    for i in arr:
        if i==0:
            sumo*=10
        elif i==3:
            pass
        else:
            sumo=sumo*10+i

    return sumo


#DO NOT change anything below this line

N=int(input())
arrNum=intToArr(N)
arrNumWithout3=remove_3(arrNum)

print(arrToInt(arrNumWithout3))
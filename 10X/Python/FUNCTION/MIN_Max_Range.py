'''
min max range
Given 3 lists of positive integers. From the first list get the minimum value m1 and second list get the maximum value m2. 
From the third list get all the values that lies between m1 and m2 including m1 and m2.

If m1 <= m2 then we should consider all the values x from third list which stisifies m1 <= x <= m2

If m1 > m2 then we should consider all the values x from third list which stisifies m1 >= x >= m2

You have write 3 functions.

Takes list as input and returns a minimum value.
Takes list as input and returns a maximum value.
Takes a list, m1 and m2 and returns list of intergers which lies between m1 and m2. If no such numbers exist return a 
list with -1 i.e [-1]
You have to return the list of numbers in the same order they are present.

You will be provided with function template, you have to fill those functions.

Input
[3,5,4,5,7]

[7,6,4,4,23,2]

[6,5,1,3,8,9,2]

Output
[6,5,3,8,9]

'''
'''
def maximum_value(input_numbers):
    # write below this here
    m2 = max(input_numbers)
    return m2

## This function should return single integer. 
## The integer should be minimum value of input list
def minimum_value(input_numbers):
    # Please write below this
    m1 = min(input_numbers)
    return m1
    
'''

## This function should return single integer. The integer should be maximum value of input list
## Please fill the following function
def maximum_value(input_numbers):
    # write below this here
    if input_numbers:
         m2 = max(input_numbers)
         return m2
    else:
        return 0
## This function should return single integer. 
## The integer should be minimum value of input list
def minimum_value(input_numbers):
    # Please write below this
    if input_numbers:
         m1 = min(input_numbers)
         return m1
    else:
        return 0
    

## This function should return list of integer which lies between m1 and m2. 
## if m1 <= m2 return list off numbers between m1 and m2
## if m2 <= m1 return list off numbers between m2 and m1
def get_numbers_in_range(input_numbers, m1, m2):
    # Please write below this line
    a=[]
    #n=len(input_numbers)
    if m1<=m2:
        for i in input_numbers:
            if i>=m1 and i<=m2:
                a.append(i)

    if m1>=m2:
        for i in input_numbers:
            if i<=m1 and i>=m2:
                a.append(i)
                
    if a:
        return a
    else:
        return -1



### Please do not change anything below this line.
if __name__ == "__main__":
    list1 = [int(i) for i in input().split(' ')]
    list2 = [int(i) for i in input().split(' ')]
    list3 = [int(i) for i in input().split(' ')]
    m1 = minimum_value(list1)
    m2 = maximum_value(list2)
    min_max_range = get_numbers_in_range(list3, m1, m2)
    [print(i) for i in min_max_range]
'''
Even Odd Separator
Write a function which takes a list of positive integers and return a list with all the odd numbers at the start followed by even numbers.

All the odd numbers should appear in the same order as they present, similarly the even number.

Input
A list of positive integers

Output
list of integers

Example
Input:

[2,5,4,10,1,3,7,8,11,13,6]

Output:

[5,1,3,7,11,13,2,4,10,8,6]

'''
# Write a function with name even_odd_separator, you should exactly the same name
# This even_odd_separator functions should take a list of integers and return a list
# you can start from here
def even_odd_separator(numbers):
    even=[]
    odd=[]
    for i in numbers:
        if (i%2==0):
            even.append(i)
        else:
            odd.append(i)
    return odd+even


### Do not change anything below this line
if __name__ == "__main__":
    numbers = [int(i) for i in input().split(' ')]
    separated = even_odd_separator(numbers)
    for num in separated:
    	print(num)
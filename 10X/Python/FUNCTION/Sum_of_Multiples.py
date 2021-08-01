"""
Sum of Multiples
Write a function which takes a list L of positive intergers and a positive integer N(N > 0) and returns the sum of all the intergers of the list L which are multiples of N.

Input
Write a function sum_of_multiples which takes a list and an integer

Output
integer

Example
Input:

[1,2,3,4,5,6,7], 3 inputs for function

Output:

9

"""
# Write function with name sum_of_multiples which takes a list and integer
# It should return sum of multiple of integer given.
# You can start from here
def sum_of_multiples(numbers, mult):
    sum=0
    for i in numbers:
        if (i%mult==0):
            sum+=i
    return sum

	
	
	
# Do not change anything below this line
if __name__ == "__main__":
    numbers = [int(i) for i in input().split(' ')]
    mult = int(input())
    print(sum_of_multiples(numbers, mult))
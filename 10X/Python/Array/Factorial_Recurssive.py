"""
Factorial: Recursive
Description
Write a program that computes the factorial of a given integer. Your implementation should be recursive in nature. Factorial of an integer n is defined as

Factorial(n) = undefined, if n < 0
             = 1, if n is 0
             = n*Factorial(n-1), otherwise
Input format
One line containing an integer n.

Output format
One line containing the factorial of n.

Sample input
5
Sample output
120
Explanation
Factorial of 5 is 5*4*3*2*1*1 which is 120.

Sample input
-4
Sample output
undefined
Explanation
Factorial of a negative integer is undefined.
"""
"""
def factorial(n):
    # Implement this function
    if n<0:
    	return "undefined"
    elif n==0:
    	return 1
    elif n==1:
    	return 1
    else:
    	n*=factorial(n-1)
        return n

# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    print(factorial(n))
"""
def factorial(n):
    # Implement this function
    if n<0:
    	return "undefined"
    elif n==0:
    	return 1
    elif n==1:
    	return 1
    else:
        n*=factorial(n-1)
        return n

# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    print(factorial(n))
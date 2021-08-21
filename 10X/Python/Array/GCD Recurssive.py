"""
GCD: Recursive
Description
Write a program that computes the GCD of two positive integers using Euclid's algorithm. Your implementation should be recursive in nature. Given two positive integers a, b (a >= b), Euclid's algorithm is defined as follows.

GCD(a, b) = b, if b is a divisor of a
          = GCD(b, a%b), otherwise
Input/Output format
You only need to implement the gcd function provided in the template. The template takes care of reading the input, passing it on to gcd function and printing the result.

"""
def gcd(a, b):
    # Implement this function
	if a%b==0:
		return b
	return gcd(b, a%b)
# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    for index in range(n):
        inputInts = input().split(' ')
        dividend = int(inputInts[0])
        divisor = int(inputInts[1])
        print(gcd(dividend, divisor))
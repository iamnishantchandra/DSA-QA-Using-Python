'''
367. Valid Perfect Square
----------------------------
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1

link-- " https://leetcode.com/problems/valid-perfect-square/ "


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
'''
no=int(input())
n=int(no**.5)
if n==(no*no):
    print(True)
else:
    print(False)
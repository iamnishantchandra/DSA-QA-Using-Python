'''
Handle Strings
You have been given n string values. Lets say the given values are a1, a2, a3, a4 ...

For each string, you need to print:

foo, if length of the string is divisible by 3.
bar, if length of the string is divisible by 5.
foobar, if length of the string is divisible by 3 and 5 both.
- , otherwise.
Note:
Strings may contain symbols like #, $, @, etc
Solve this without using array.
Input Format:
First line denotes n, the number of inputs. The next n lines contains one string in each line.

Output Format:
One string denoting the result, as mentioned above.

Example:
Input:

5
10
-20
abcde
40@$#@^*
5sfgsge6543
Output:

-
foo
bar
-
-

'''
n=int(input())
for i in range(n):
    s=len(input())
    if s==0:
        print("-")
    elif s%15==0:
        print("foobar")
    elif s%5==0:
        print("bar")
    elif s%3==0:
        print("foo")
    else:
        print("-")



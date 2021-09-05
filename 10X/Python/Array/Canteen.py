'''
Canteen
You and Ravi, are deciding how to split bill at canteen. Each will only pay for the items they consume. Ravi gets the check and calculates your portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: bill = [2,4,6]. You declined to eat item k = bill[2] which costs 6. If Ravi calculates the bill correctly, you will pay (2 + 4)/2 = 3. If he includes the cost of bill[2], he will calculate (2 + 4 + 6)/2. In the second case, he should refund 3 to you.

Input Format
The first line contains two space-separated integers n and k, the number of items ordered and the 0-based 
index of the item that you did not eat.

The second line contains n space-separated integers where 0 ≤ i < n.

The third line contains an integer, b, the amount of money that Ravi charged You for your share of the 
bill.

Note:
The amount of money due to you by Ravi will always be an integer.
Output Format
If Ravi did not overcharge you, print It is Correct! on a new line; otherwise, print the difference 
(i.e., bcharged - bactual) that Ravi must refund to you. This will always be an integer.

Sample Input
4 1
3 10 2 9
12
Sample Output
5
Explanation
You didn't eat item bill[1] = 10, but she shared the rest of the items with Brian. The total cost of the 
shared items is 3 + 2 + 9 = 14 and, split in half, the cost per person is bactual = 7. Ravi charged you 
bcharged = 12 for your portion of the bill. We print the amount you were overcharged, 
bcharged - bactual = 12 - 7 = 5, on a new line.
'''
# your code goes here
n,k=map(int,input().split())
ar=[int(x) for x in input().split()]
p=int(input())
s=(sum(ar)-ar[k])//2
if p>s:
	print(p-s)
else:
	print("It is Correct!")
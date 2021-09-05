'''
Restaurant Orders
You are managing a restaurant. The restaurant contains t tables. Each time a table orders food, you receive a tuple containing the table number and cost of the item. In total you are given n orders. You add the cost to their bill. Given a list of orders, find the table that has the highest bill. If there are multiple tables with the same bill number, print out all of the restaurants with highest bill line by line in ascending order

Input
First line contains n, n >= 0, denoting the number of total orders in the restaurant. 
Next line contains t denoting the number of tables in the restaurant. It is followed by 2n lines The 
first n lines denote the table number of the order. Each table number is i >= 1 Next n lines denote the 
bill amount for the corresponding order

Output
m lines. Each line an integer, denoting the table number with the highest bill values

Example
Input:

5
4
1
2
3
4
3
100
200
300
500
200
Output:

3
4
The first line is 5, denoting the number of orders in the list 1,2,3,4,3 are the table numbers of the 
orders in sequence 100, 200, 300, 500, 200 are the bill values for the orders The highest bill is 500 for 
the table 3 and 4, so both of them are printed out one after the other in ascending order

'''
a=[]
n=int(input())
t=int(input())
d={}
ma=0
for _ in range(int(n*2)):
    a.append(int(input()))
for i in range(n):
    if a[i] in d:
        d[a[i]]+=a[i+n]
        if d[a[i]]>ma:
            ma=d[a[i]]
    else:
        d[a[i]]=a[i+n]
        if d[a[i]]>ma:
            ma=d[a[i]]
for i in d:
    if ma==d[i]:
        print(i)

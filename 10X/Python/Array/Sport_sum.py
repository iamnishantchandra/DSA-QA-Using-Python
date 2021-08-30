"""
Sports Stats
Max likes football very much. In order to check the popuplarity of the game, he decided to talk to random people and ask them about their favourite game and note it down in a list.

Given a list of name of people and their favourite sport, help Max in finding the sport liked by most of the people, and also how many people like football.

He could have met same people more than once, he will only count response of his first meet with any person.

Note : Name of person as well as sport is a single string in lowercase. Length of name of people as well as sport is less than 11.

Input
First line will contain no of entries in the list. i.e. N Next N lines will contain two strings, person's name and sports he like.

Output
In first ine, name of sport liked by most no of people (In case of more than one games is liked by highest no of people, output the first one in lexicographical order). In second line, no of people having football as their favourite game.

Example
Input:

7

abir cricket

aayush cricket

newton kabaddi

abhinash badminton

sanjay tennis

abhinash badminton

govind football

Output:

cricket

1

Explanation
2 people likes cricket, ans so it liked by maximum people. 1 person has football as his favourite sport
"""
'''
d={}
max=0
sports=""
for _ in range(int(input())):
    data=input().split(" ")
    d[data[0]]=data[1]
for key in d:
    count=0
    for j in d:
        if d[key]==d[j]:
        #if key==j:
            count=count+1
            if count>max:
                max=count
                sports=d[key]
print(sports)        
find="football"
count=0
for key in d:
    if d[key]==find:
        count+=1
print(count)

#80%
'''
d={}
max=0
# sports=""
nd={}
sp=""
for _ in range(int(input())):
    data=input().split(" ")
    d[data[0]]=data[1]
for i in d:
    j=d[i]
    if j in nd:
        nd[j]+=1
    else:
        nd[j]=1
for i in sorted(nd):
    if nd[i]>max:
        max=nd[i]
        sp=i
print(sp)
# for i in d:
#     if d[i]==sp:
#         sports=d[i]
find="football"
count=0
for key in d:
    if d[key]==find:
        count+=1
print(count)

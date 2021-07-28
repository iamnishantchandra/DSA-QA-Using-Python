a=input()
n=len(a)
R=0
G=0
for i in range(n):
    if a[i]=='R':
        R+=1
    else:
        G+=1

print(min(R,G))
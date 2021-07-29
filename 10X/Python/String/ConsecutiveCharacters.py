#ConsecutiveCharacters
s=input()
l=len(s)
if l>0:
    
    prev=''
    count=0
    prev=s[1]
    max=0
    for i in range(0,l-1):
        if (prev==s[i]):
            count+=1
        else:
            prev=s[i+1]
            count=0
        if max<count:
            max=count
    print(max)
    
else:
    print(0)

"""
        count=1
        maxi=0
        for i in range(1,len(s)):
            if (s[i]==s[i-1]):
                count+=1
            else:
                maxi=max(count,maxi)
                count=1
        print(max(count,maxi))


"""



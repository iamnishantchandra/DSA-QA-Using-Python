a1,a2,a3=map(int,input().split())
b1,b2,b3=map(int,input().split())

prl=((((a2*b3)-(a3*b2))**2)-(((a1*b3)-(b1*a3))**2)+(((a1*b2)-(a2*b1))**2))
perd=((a1*b1)+(a2*b2)+(a3*b3))
if (prl==0):
    print("1")
elif(perd==0):
    print("2")
else:
    print("0")





'''
A.B = a1 x b1 + a2 x b2 + a3 x b3

A x B = (a2 x b3 - a3 x b2) i - (a1 x b3 - b1 x a3) j + (a1 x b2 - a2 x b1) k

|A|2 = a12 + a22 + a32

If A.B = 0, then A and B are perpendicular.

If |A X B| = 0, then A and B are parallel.


'''
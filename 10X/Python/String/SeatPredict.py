n=int(input())
for i in range(n):
    t,s=map(int,input().split())
    if (t>=s and t>0 and s>0):
        if(s%8==1 or s%8==4):
             print("L")
        elif(s%8==2 or s%8==5):
             print("M")
        elif(s%8==3 or s%8==6):
             print("U")
        
        elif(s%8==7):
             print("SL")
        elif(s%8==0):
             print("SU")
    else:
        print("Invalid")   

        '''
        elif(s%8==4):
            print("L")
        elif(s%8==5):
            print("M")
        elif(s%8==6):
             print("U")
        '''
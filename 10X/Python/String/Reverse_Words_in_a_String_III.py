a=input().split()
d=''
for i in range(len(a)):
    s=a[i]
    c=(len(s)+1)
    d=d+s[-1:-c:-1]+' '
print(d) 


'''
class Solution:
    def reverseWords(self, s: str) -> str:
        z=len(s)
        a=s.split()
        d=''  
        for i in range(len(a)):
        
            d=d+a[i][::-1]+' '
           #d=d+' '+a[i][::-1]
            
        return d[0:z:]
        #return d[1] 

        '''


'''
class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(" ")
        reversed_words = []
        
        for word in word_list:
            reversed_words.append(word[::-1])
        
        return " ".join(reversed_words)



        '''
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        d=''        
        for i in s:  
            d+=i[::-1]+' '
            
        return d[0:len(d)-1:]
    
    
   

        '''
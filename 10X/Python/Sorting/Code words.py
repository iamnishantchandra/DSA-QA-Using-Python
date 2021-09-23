"""
Code Words
Description
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Input format
First line contains a positive integer n, denoting the number of test cases. It is followed by n lines. Each of the n lines contains space separated words.

Output format
n lines containing the number of different transformations among all words we have.

Sample input
1
gin zen gig msg
Sample output
2
Explanation
The transformation of each word is:

"gin" -> "--...-."

"zen" -> "--...-."

"gig" -> "--...--."

"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".

Note
The length of words will be at most 100000

Each words[i] will have length in range [1, 12].

words[i] will only consist of lowercase letters.

"""
#a=97
#z=97+25=122 ord("z")
###########################   BY USING DICT  ######################

'''
# your code goes here
def morsh(ss):
    dic={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}              
    s=""
    for i in range(len(ss)):
        if ss[i] in dic:
            s+=dic[ss[i]]
    return s

def check(ar):
    dic1={}
    for i in range(len(ar)):
        temp=morsh(ar[i])
        if temp in dic1:
            dic1[temp]+=1
        else:
            dic1[temp]=1
    return len(dic1)

for _ in range(int(input())):
    ar=input().split()
    print(check(ar))

'''
################### FOR ONLY small(a-z) #########################
'''
def morshword(ss):
    dic={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--.."}              
    s=""
    for i in range(len(ss)):
        if ss[i] in dic:
            s+=dic[ss[i]]
    return s

def check(ar):
    dic1={}
    for i in range(len(ar)):
        temp=morshword(ar[i])
        if temp in dic1:
            dic1[temp]+=1
        else:
            dic1[temp]=1
    return len(dic1)

for _ in range(int(input())):
    ar=input().split()
    print(check(ar))


'''

###########################   BY USING ARRAY AND ASCII VALUE  ######################
def morsh(ss):
    dic=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    s=""
    for i in ss:
    	s += dic[ord(i)-97]
    return s
def check(ar):
    dic1={}
    for i in range(len(ar)):
        temp=morsh(ar[i])
        if temp in dic1:
            dic1[temp]+=1
        else:
            dic1[temp]=1
    return len(dic1)

for _ in range(int(input())):
    ar=input().split()
    print(check(ar))
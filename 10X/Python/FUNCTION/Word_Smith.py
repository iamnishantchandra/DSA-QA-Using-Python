"""
Word Smith
------------
You are a word-smith and you modify strings according to peoples requirements. Lately there has been a 
great demand for removing certain letters from the strings provided. Instead of taking the strings and 
doing the manual process of removing the letters, you started selling functions which does the same task. 
The user will provide a list of alphabets and you will provide them with a functions which takes a string 
and removes those alphabets given by the customer.

Now you have to write a function f1 which takes a list of alphabets and returns a function f2 which 
takes a string and removes all the alphabets provided to the function f1.

Input
-------
list of alphabets.

Output
-------
A functions which takes string as input and returns a string by removing all the alphabets provided in 
the above function.

Example
Input:

[a,d,r]

Output:

function which takes string as input and returns a string by removing a,d,r
"""
# This function should return a function which takes string as input 
# removes all the alphabets which are present in the forbidden_alphabets list
# forbidden_alphabets is a list off alphabets
# Your returned function should take string as input returns a string 
# by removing forbidden alphabets
def word_smith(forbidden_alphabets):

    # You can start from here
    for i in forbidden_alphabets:
    
		
		



### Do not change anything below this line.
if __name__ == "__main__":
    alphabets = [i for i in input().split(' ')]
    input_string = input()
    chopper = word_smith(alphabets)
    print(chopper(input_string))
def string_repeat(string_to_repeat, repeat):
    # Write from here
    s=""
    a=int(repeat)
	
    s=(string_to_repeat+" ")*(a-1)
    s+=string_to_repeat
    return s

'''
    s=""
    for i in range(int(repeat)-1):
    	s+=string_to_repeat+" "
    s+=string_to_repeat
    return(s)
    '''
"""
	s=''
    for i in range(int(repeat)-1):
        s+=string_to_repeat+" "
    s=s+string_to_repeat
    return(s,repeat)
    """



# Please don't change anything below this line.
# You don't have to worry about reading input, just fill the function above.

if __name__ == "__main__":
    input_string = input()
    input_number = input()
    print(string_repeat(input_string, input_number))
'''
Remove First Alphabet
Write a function which takes a list of strings and returns the list by removing the first letter from each string.

If only one letter is present in the string, delete that element from the list.

The function name should be remove_first_alphabet

Input
list of string

Output
list of strings

Example
Input:

['adf', 'qwert', 'a', 'rewq']

Output:

['df', 'wert', 'ewq']

'''
# Write function with name remove_first_alphabet which takes a list of string
# Remove first letter from each string and return the list
def remove_first_alphabet(alpha):
    list1=[]
    for i in alpha:
        a=i[1:len(i)]
        list1.append(a)
    return list1
# Do not change anything below this line
if __name__ == "__main__":
    alpha = [i for i in input().split(' ')]
    removed_list = remove_first_alphabet(alpha)
    [print(i) for i in removed_list]

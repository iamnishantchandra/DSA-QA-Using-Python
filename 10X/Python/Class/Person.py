'''
Person
Define a class named Person, which should have the name and age as the properties. You don't need to worry about input/output and object of the class. The given template will take care of it.

The input will contain the name and age. The same will be printed in seperate lines as output.

Input
One line containing two space seperated values, denoting name and age respectively.

Output
Print name and age in newline each.

Example
Input1:

Jonny 15
Output1:

Jonny
15
'''
### Define the required class here...
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age


### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__ == '__main__':
    
    input_string = input().split()

    p1 = Person(input_string[0], int(input_string[1]))

    print(p1.name)
    print(p1.age)

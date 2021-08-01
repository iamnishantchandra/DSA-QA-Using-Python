"""
def greeting(first_name, last_name):
    print('Hello,',first_name, last_name)

greeting(last_name='Last', first_name='First')

def sample_problem(*arg):
    for val in arg:
        print(val)
sample_problem(1,2,3,4,5)

def sample_problem_2(**kwargs):
    print(kwargs)
    print(kwargs['a'])
    print(kwargs['b'])
    print(kwargs['c'])
    print(kwargs['d'])

    
sample_problem_2(a=1, b=2, c=3, d=4)
"""
list1=["are","ramaa","rohan"]
list2=[]
for i in list1:
    a=i[1:len(i)]
    list2.append(a)
print(list2)

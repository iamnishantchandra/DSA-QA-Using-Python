def printer(i_list):
    for i in i_list:
        print_with_index(i, i_list[i])
    
	


# Do not change anything below this line
def print_with_index(index, current_string):
    print(index, current_string)

if __name__ == "__main__":
    count = int(input())
    input_list = [input() for i in range(count)]
    printer(input_list)
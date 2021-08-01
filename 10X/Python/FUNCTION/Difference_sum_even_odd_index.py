


def difference_sum_even_odd_index(num):
    even=0
    odd=0
    if len(num)==1:
        odd=0
    for i in num:
        if (num.index(i)==0 or num.index(i)%2==0):
            even+=i
        else:
            odd+=i
    return(even-odd)
        



if __name__ == "__main__":
    numbers = [int(i) for i in input().split(' ')]
    print(difference_sum_even_odd_index(numbers))
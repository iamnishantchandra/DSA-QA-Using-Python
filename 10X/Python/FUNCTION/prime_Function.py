import math
def is_prime(input_number):
    # You can start below this
    if(input_number<=1):
        return False
    if(input_number>2):
        for i in range(2,int(math.sqrt(input_number)+1)):
            if input_number%i==0:
                return False
        return True
    if(input_number==2):
        return True
        
#2,((input_number//2)+1)
#2,int(math.sqrt(input_number)+1)

### Please don't change anything below this line.
if __name__ == "__main__":
    number = int(input())
    print(is_prime(number))
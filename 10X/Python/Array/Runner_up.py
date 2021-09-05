if __name__ == '__main__':
    n = int(input())
    arr =[int(x) for x in input().split()]
    ma=-10000
    sec=ma
    a=[]
    for i in range(n):
        if arr[i]>sec and arr[i]!=ma:
            sec=arr[i]
            if sec>ma:
               ma,sec=sec,ma

    print(sec)
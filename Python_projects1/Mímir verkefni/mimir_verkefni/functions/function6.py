def fibo(n):
    counter = 0
    tala1 = 1
    print(tala1, end=' ')
    tala2 = 1
    print(tala1, end=' ')

    while counter < n-2:
        fibo_num = tala1 + tala2
        print(fibo_num, end=' ')
        tala2 = tala1
        tala1 = fibo_num
        counter += 1    

n = int(input("Input the length of Fibonacci sequence (n>=1): "))
if n == 1:
    tala1 = 1
    print(tala1)
elif n >= 2:    
    fibo(n)   
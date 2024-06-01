def square(N):
    num = 1
    for i in range(N):
        for _ in range(N):
            print(num,end=' ')
            num += 1
            if num == 10: num = 1
        print()

square(int(input()))
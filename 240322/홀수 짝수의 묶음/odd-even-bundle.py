n = int(input())
nums = list(map(int,input().split()))

odd, even = 0, 0
for num in nums:
    if num%2: odd += 1
    else: even += 1

if odd == even: print(odd*2)
elif odd > even:
    while odd > even:
        odd -= 2
        even += 1
    if odd == even or odd+1 == even: print(odd+even)
    else:
        print(odd+even-1)
else:
    print(odd*2+1)
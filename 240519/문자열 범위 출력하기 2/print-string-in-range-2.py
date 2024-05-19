word = input()
n = int(input())

ans = word[-n:]
print(ans[::-1])
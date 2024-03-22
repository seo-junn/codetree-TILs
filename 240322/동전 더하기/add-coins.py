import sys

n, k = map(int,sys.stdin.readline().split())
coins = list(map(int,sys.stdin.read().splitlines()))

count = 0
coin = n-1
while k > 0 and coin >= 0:
    count += k//coins[coin]
    k %= coins[coin]
    coin -= 1

print(count)
max_benefit = 0
n = int(input())
prices = list(map(int,input().split()))
max_prices = [0]*n

temp = 0
for i in range(n-1,-1,-1):
    if prices[i] > temp: temp = prices[i]
    max_prices[i] = temp

for i in range(n):
    temp_benefit = max_prices[i]-prices[i]
    if temp_benefit > max_benefit:
        max_benefit = temp_benefit

print(max_benefit)
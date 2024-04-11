import sys

n = int(sys.stdin.readline())
energy_consumption = list(map(int,sys.stdin.readline().split()))
charge_costs = list(map(int,sys.stdin.readline().split()))

min_val = sys.maxsize
min_cost = []
for i in range(n):
    if charge_costs[i] < min_val:
        min_val = charge_costs[i]
    min_cost.append(min_val)

total_cost = 0
for i in range(n-1):
    total_cost += min_cost[i]*energy_consumption[i]

print(total_cost)
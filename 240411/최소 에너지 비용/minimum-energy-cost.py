import sys

n = int(sys.stdin.readline())
energy_consumption = list(map(int,sys.stdin.readline().split()))
charge_costs = list(map(int,sys.stdin.readline().split()))

min_cost = [0]*(n-1)
acc_energy = energy_consumption[-1]
min_cost[n-2] = energy_consumption[-1]*charge_costs[n-2]
for i in range(n-3,-1,-1):
    acc_energy += energy_consumption[i]
    min_cost[i] = min(acc_energy*charge_costs[i],min_cost[i+1]+energy_consumption[i]*charge_costs[i])

print(min_cost[0])
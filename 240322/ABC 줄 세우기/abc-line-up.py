n = int(input())
people = input().split()

def swap(i,j):
    temp = people[j]
    people[j] = people[i]
    people[i] = temp

count = 0
for i in range(n):
    for j in range(i,n):
        if people[i] > people[j]:
            swap(i,j)
            count += 1

print(count)
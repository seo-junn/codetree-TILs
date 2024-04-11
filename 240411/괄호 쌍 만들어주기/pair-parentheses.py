line = input()

opened = [0]*len(line)
closed = [0]*len(line)

for i in range(1,len(line)):
    if line[i] == '(' and line[i-1] == '(': opened[i] = 1

count = 0
for i in range(len(line)-2,-1,-1):
    if line[i] == ')' and line[i+1] == ')': count += 1
    closed[i] = count

total_count = 0
for i in range(len(line)-1):
    total_count += opened[i]*closed[i+1]

print(total_count)
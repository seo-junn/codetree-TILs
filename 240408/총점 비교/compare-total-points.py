n = int(input())
students = []

for _ in range(n):
    name, *subs = input().split()
    subs = list(map(int,subs))
    students.append((name,*subs))

students.sort(key=lambda x:x[1]+x[2]+x[3])
for student in students:print(*student)
base = []

for _ in range(5):
    name, h, w = input().split()
    base.append((name,int(h),float(w)))
    
base.sort(key=lambda x:x[0])
print('name')
for item in base: print(*item)
print()
base.sort(key=lambda x:-x[1])
print('height')
for item in base: print(*item)
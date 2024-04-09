base = []

while True:
    age = int(input())
    if age // 10 == 2: base.append(age)
    else: break

print("%.2f"%(sum(base)/len(base)))
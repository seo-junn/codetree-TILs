n = int(input())
avg = sum(map(float,input().split()))/n

print(f'{avg:.1f}')
if avg >= 4.0: print("Perfect")
elif avg >= 3.0: print("Good")
else: print("Poor")
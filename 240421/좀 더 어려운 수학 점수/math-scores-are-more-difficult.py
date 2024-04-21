am,ae = map(int,input().split())
bm,be = map(int,input().split())

if am == bm:
    print('A' if ae > be else 'B')
else:
    print('A' if am > bm else 'B')
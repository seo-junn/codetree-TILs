from itertools import product

alp = 'abcdef'
formula = list(input().strip())
max_res = 0
for item in product(range(1,5),repeat=6):
    base = {}
    for i in range(6):
        base[alp[i]] = item[i]
    res = base[formula[0]]
    for i in range(1,len(formula),2):
        if formula[i] == '+':
            res += base[formula[i+1]]
        elif formula[i] == '-':
            res -= base[formula[i+1]]
        else:
            res *= base[formula[i+1]]
    max_res = max(max_res,res)

print(max_res)
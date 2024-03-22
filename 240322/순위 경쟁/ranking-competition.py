n = int(input())

base = {'A':0,'B':0,'C':0}
prize = 'ABC'

count = 0
for _ in range(n):
    c,s = input().split()
    base[c] += int(s)

    if base['A'] == base['B'] == base['C']: n_prize = 'ABC'
    elif base['A'] == base['B']:
        n_prize = 'AB' if base['A'] > base['C'] else 'C'
    elif base['B'] == base['C']:
        n_prize = 'BC' if base['B'] > base['A'] else 'A'
    elif base['A'] == base['C']:
        n_prize = 'AC' if base['A'] > base['B'] else 'B'
    else:
        n_prize = ''
        val = -10**7
        for c in 'ABC':
            if base[c] > val:
                val = base[c]
                n_prize = c

    if n_prize != prize:
        count += 1
        prize = n_prize

print(count)
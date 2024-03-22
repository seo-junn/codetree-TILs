n = int(input())

score = {'A':0,'B':0}
prize = 'AB'

count = 0
for i in range(n):
    c,s = input().split()
    score[c] += int(s)

    if score['A'] == score['B']: n_prize = 'AB'
    elif score['A'] > score['B']: n_prize = 'A'
    else: n_prize = 'B'

    if prize != n_prize: count += 1
    prize = n_prize

print(count)
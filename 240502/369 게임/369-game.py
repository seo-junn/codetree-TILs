game = []
for num in range(1,int(input())+1):
    if '3' in str(num) or '6' in str(num) or '9' in str(num) or num%3 == 0:
        game.append(0)
    else:
        game.append(num)

print(*game)
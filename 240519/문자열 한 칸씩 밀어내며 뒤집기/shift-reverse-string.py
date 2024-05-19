word,q = input().split()
for _ in range(int(q)):
    c = int(input())
    if c == 1:
        word = word[1:] + word[0]
    elif c == 2:
        word = word[-1] + word[:-1]
    else:
        word = word[::-1]
    print(word)
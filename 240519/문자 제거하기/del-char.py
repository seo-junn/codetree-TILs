word = list(input())
while len(word) > 1:
    n = int(input())
    if n < len(word): word.pop(n)
    else: word.pop()
    print(''.join(word))
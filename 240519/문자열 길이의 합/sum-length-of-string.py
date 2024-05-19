total_length, count_a = 0,0

for _ in range(int(input())):
    word = input()
    total_length += len(word)
    if word[0] == 'a': count_a += 1

print(total_length,count_a)
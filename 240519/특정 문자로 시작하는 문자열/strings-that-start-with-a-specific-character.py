count, total_length = 0,0

words = []
for _ in range(int(input())): words.append(input())
c = input()

for word in words:
    if word[0] == c:
        count += 1
        total_length += len(word)

print(count,f'{total_length/count:.2f}')
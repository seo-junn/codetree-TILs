words = []
for _ in range(10): words.append(input())
c = input()

count = 0
for word in words:
    if word[-1] == c:
        print(word)
        count += 1

if count == 0: print("None")
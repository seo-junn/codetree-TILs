def palindrome(string):
    return string == string[::-1]

line = input()
print("Yes" if palindrome(line) else "No")
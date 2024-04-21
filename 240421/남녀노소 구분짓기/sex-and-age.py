sex = int(input())
age = int(input())

if age >= 19:
    print('WOMAN' if sex else 'MAN')
else:
    print("GIRL" if sex else 'BOY')
base = {'S':'Superior','A':'Excellent','B':'Good','C':'Usually','D':'Effort'}

c = input()
print(base[c] if c in base else 'Failure')
score = int(input('score:'))

if score > 75:
    credit = 'A'
elif score > 50:
    credit = 'B'
elif score > 35:
    credit = 'S'
else:
    credit = 'F'

print(credit)
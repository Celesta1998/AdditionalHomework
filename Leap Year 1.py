def year_leap(a):
    if a%4 == 0:
        return True
    else:
        return False
b = year_leap(int(input('Введите год: ')))
print(b)


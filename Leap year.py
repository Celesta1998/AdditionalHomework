a = int(input())
if a % 4 != 0:
    print('Common year/Обычный год')
elif a % 100 == 0:
    if a % 400 == 0:
        print('Leap year/Високосный год')
    else:
        print('Common year/Обычный год')
else:
    print('Leap year/Високосный год')



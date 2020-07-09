import sys
try:
    x=sys.argv[1]


    if int(x) > 100:
        raise ValueError
except ValueError:
     print('cant take the input value')

else:
    for i in range(int(x)):
        if i % 2 == 0:
            if i in [40, 62, 70]:
                print(f'number:{i} in process')
                continue
            elif i == 80:
                print('cannot process more than 100')
                break
            else:
                print(i)

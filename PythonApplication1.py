a = 1
for i in range(1, 101):
    for b in str(i):
        if b == '7':
            if a % 2 == 0:
                print(str(i))
            else:
                print(str(i))
                a += 1

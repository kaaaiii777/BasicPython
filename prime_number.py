
# TODO
a, b = 61, 10
if a <= 1:
    print(False)
else:
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            print(False)
            break
    else:
        print(True)


if b <= 1:
    print(False)
else:
    for i in range(2, int(b **0.5) + 1):
        if b % i == 0:
            print(False)
            break
    else:
        print(True)
        




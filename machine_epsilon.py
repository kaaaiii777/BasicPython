x = 1

def kyokugen():
    global x
    while 1 + x > 1:
        x = 0.5 * x
    print(x * 2)

kyokugen()
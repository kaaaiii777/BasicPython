

#(1)
a, b = 10, 20
if a < b :
    if b % a == 0:
        print(a)
    else:
        while b % a != 0 :
            b, a = a, b % a
            print(a)
elif a > b :
    if a % b == 0:
        print(b)
    else:
        while a % b != 0 :
            a, b = b, a % b
            print(b)
elif a == b :
    print(a)

#(2)
a, b = 14, 91
if a < b :
    if b % a == 0:
        print(a)
    else:
        while b % a != 0 :
            b, a = a, b % a
            print(a)
elif a > b :
    if a % b == 0:
        print(b)
    else:
        while a % b != 0 :
            a, b = b, a % b
            print(b)
elif a == b :
    print(a)
    
#(3)
a, b = 91, 14
if a < b :
    if b % a == 0:
        print(a)
    else:
        while b % a != 0 :
            b, a = a, b % a
            print(a)
elif a > b :
    if a % b == 0:
        print(b)
    else:
        while a % b != 0 :
            a, b = b, a % b
            print(b)
elif a == b :
    print(a)
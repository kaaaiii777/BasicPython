
# TODO
n = 0
def sosuhantei(n) :
    if n <= 1:
        print(False)
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print(False)
            break
        else:
            print(True)

sosuhantei(61)
sosuhantei(10)
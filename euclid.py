#問３
import math
def tagainiso(a, b):
    print(math.gcd(a, b))

tagainiso(10, 20)
tagainiso(14, 91)
tagainiso(91, 14)

#問４
def sosuhantei(a, b):
    if math.gcd(a, b) == 1:
        print("true")
    else:
        print("false")

sosuhantei(10, 20)
sosuhantei(14, 91)
sosuhantei(91, 14)


#問３
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(10, 20))
print(gcd(14, 91))
print(gcd(91, 14))
#問４
def tagainiso(a, b):
    if gcd(a, b) == 1:
        return True
    else:
        return False

print(tagainiso(10, 20))
print(tagainiso(14, 91))
print(tagainiso(91, 14))


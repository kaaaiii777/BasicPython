from math import sin,pi
# --example--
# print(sin(0))
# >>> 0
# -----------
a = 0
b = pi / 2
N = 100
h = (b - a) / N
Sk = 0
S = 0

def sekibun():
    global S
    for k in range(1,N+1):
        Sk = 0.5 * h * (sin(a + (k - 1) * h) + sin(a + k * h))
        S += Sk
    print(S)

sekibun()
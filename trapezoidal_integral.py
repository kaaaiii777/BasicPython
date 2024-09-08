import math
# --example--
# print(sin(0))
# >>> 0
# -----------


def sekibun(f, a = 0, b = 1, n = 100):
    h = (b - a) / n
    Sk = 0
    S = 0
    for k in range(1,n + 1):
        Sk = 0.5 * h * (f(a + (k - 1) * h) + f(a + k * h))
        S += Sk
    return S

def f(x):
    return math.sin(x)

def g(x):
    return 4 / (1 + x ** 2)

def h(x):
    return math.sqrt(math.pi) * math.exp(-x ** 2)

print(sekibun(f, 0, math. pi / 2, 100))
print(sekibun(g, 0, 1, 100))
print(sekibun(h, -100, 100, 1000))
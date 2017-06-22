def __comp(a, b):
    (q, r, s, t) = a
    (u, v, w, x) = b
    return (q * u + r * w, q * v + r * x, s * u + t * w, s * v + t * x)


def __extr(a, x):
    (q, r, s, t) = a
    return (q * x + r, s * x + t)


def __prod(a, n):
    return __comp((10, -10 * n, 0, 1), a)


def __safe(b, n):
    a = __extr(b, 4)
    return n == a[0] // a[1]


def __cons(z, z1):
    return __comp(z, z1)


def __next(z):
    a = __extr(z, 3)
    return a[0] // a[1]


def __lfts(k):
    return (k, 4 * k + 2, 0, 2 * k + 1)


def piGenLeibniz():
    """A generator function that yields the digits of Pi
    """
    k = 1
    z = (1, 0, 0, 1)
    while True:
        lft = __lfts(k)
        n = int(__next(z))
        if __safe(z, n):
            z = __prod(z, n)
            yield n
        else:
            z = __cons(z, lft)
            k += 1


def getPiLeibniz(n):
    """Returns a list containing first n digits of Pi
    """
    mypi = piGenLeibniz()
    result = []
    if n > 0:
        result += [next(mypi) for i in range(n)]
    mypi.close()
    return result
from math import sqrt


def mul_mod(a, b, m):
    return a * b % m


def inv_mod(x, y):
    u = x
    v = y
    c = 1
    a = 0

    while u != 0:
        q = v / u
        t = c
        c = a - q * c
        a = t
        t = u
        u = v - q * u
        v = t

    a = a % y

    if a < 0:
        a = y + a

    return a


def inv_mod2 (u, v):
    u1 = 1
    u3 = u

    v1 = v
    v3 = v

    if (u & 1) != 0:
        t1 = 0
        t3 = -v
        #TODO: goto Y4
    else:
        t1 = 1
        t3 = u

    while t3 != 0:
        while (t3 & 1) == 0:
            if (t1 & 1) == 0:
                t1 = t1 >> 1
                t3 = t3 >> 1
            else:
                t1 = (t1 + v) >> 1
                t3 = t3 >> 1
                #TODO: :Y4;
        if (t3 >= 0):
            u1 = t1
            u3 = t3
        else:
            v1 = v - t1
            v3 = -t3
        t1 = u1 - v1
        t3 = u3 - v3
        if (t1 < 0):
            t1 = t1 + v


def pow_mod(a, b, m):
    r = 1
    aa = a
    while True:
        if b & 1:
            r = mul_mod(r, aa, m)
        b = b >> 1
        if b == 0:
            break
        aa = mul_mod(aa, aa, m)

    return r


def is_prime(n):
    if (n % 2) == 0:
        return 0

    r = sqrt(n)

    # TODO:
    #for (i = 3; i <= r; i += 2)
    for i in range(3, r):
        if (n % i) == 0: #TODO:
            return 0
        i += 2

    return 1


def next_prime(n):
    while is_prime(n) != 0:
        n+=1
    return n



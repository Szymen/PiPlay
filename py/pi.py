from math import sqrt, log


def mul_mod(a, b, m):
    print("{0} * {1} % {2} = {3}".format(a,b,m, a * b % m))
    return (a * b) % m


def inv_mod(x, y):
    u = x
    v = y
    c = 1
    a = 0

    while u != 0:
        q = int(v / u)
        t = c
        c = int(a - q * c)
        a = t
        t = u
        u = int(v - q * u)
        v = t

    a = int(a % y)

    if a < 0:
        a = int(y + a)

    return a


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
    if n % 2 == 0:
        return False

    r = sqrt(n)
    for i in range(3, int(r+1), 2):
        if n % i == 0:
            return False

    return True


def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n


def get_n_ditit_pi(n):
    if n <= 0:
        return -1

    N = int((n+20) * log(10) / log(2))
    sum = 0

    a = 3
    while a <= 2*N:
        vmax = int(log(2*N) / log(a))
        av = 1

        for i in range(vmax):
            av *= a

        s = 0; num = 1; den = 1; v = 0; kq = 1; kq2 = 1;

        for k in range(1, N+1):
            #print("a")
            t = k

            if kq >= a:
                while True:
                    #print("petla?")
                    t = int(t/a)
                    v -= 1
                    if t % a == 0:
                        break
            kq += 1
            num = mul_mod(num, t, av)

            t = 2 * k - 1

            if kq2 >= a:
                if kq2 == a:
                    while True:
                        t = int(t/a)
                        v += 1
                        if t % a == 0:
                            break
                kq2 -= a

            den = mul_mod(den, t, av)
            kq2 += 2

            if v > 0:
                t = inv_mod(den, av)
                t = mul_mod(t, num, av)
                t = mul_mod(t, k, av)
                for i in range(vmax):
                    t = mul_mod(t, a, av)
                s += t

                if s >= av:
                    s -= av

        t = pow_mod(10, n-1, av)
        s = mul_mod(s, t, av) * 1000
        sum += s/v
        #sum %= 1.0
        a = next_prime(a)
    return sum

if __name__ == "__main__":
    print(get_n_ditit_pi(1))
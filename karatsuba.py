def karatsuba(x, y):
    # Base case
    x = str(x)
    if len(x) == 1:
        return int(x) * int(y)
    else:
        y = str(y)

        z = int(len(x) / 2)

        a = x[:z]
        b = x[z:]
        c = y[:z]
        d = y[z:]

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad = karatsuba(a, d)
        bc = karatsuba(b, c)

        return 10 ** (z * 2) * ac + 10 ** z * (ad + bc) + bd


# ===================== More general variant =========================
# al1, bl1, cl1, dl1 = ([],)*4
def karat(x, y):
    """ Not work only for two negative numbers. """
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        m = max(len(str(x)), len(str(y)))
        m2 = m // 2

        a = x // 10 ** (m2)
        b = x % 10 ** (m2)
        c = y // 10 ** (m2)
        d = y % 10 ** (m2)

        # For debug:
        # al1.append(a)
        # bl1.append(b)
        # cl1.append(c)
        # dl1.append(d)

        z0 = karat(b, d)
        z1 = karat((a + b), (c + d))
        z2 = karat(a, c)

        return (z2 * 10 ** (2 * m2)) + ((z1 - z2 - z0) * 10 ** (m2)) + (z0)


if __name__ == "__main__":
    a = 3141592653589793238462643383279502884197169399375105820974944592
    b = 2718281828459045235360287471352662497757247093699959574966967627
    print(karatsuba(a, b) == karat(a, b))
    print(karat(-999, 999))

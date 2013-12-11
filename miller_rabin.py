def miller_rabin_base_2(n):
    """Perform the Miller Rabin primality test base 2"""
    d = n-1
    s = 0
    while d % 2 == 0: # Factorise n as (2^s) * d
        d = d / 2
        s += 1

    a = 2 # Because this is the base 2 test
    x = (a**d) % n
    if x == 1 or x == n-1:
        return True
    for i in xrange(s-1):
        x = (x**2) % n
        if x == 1:
            return False
        elif x == n - 1:
            return True
    return False

def miller_rabin():
    pass
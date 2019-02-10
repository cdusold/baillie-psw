def miller_rabin_base_2(n):
    """Perform the Miller Rabin primality test base 2"""
    d, s = n - 1, 0
    while not d & 1:
        d, s = d >> 1, s + 1

    x = pow(2, d, n)
    if (x == 1) or (x == n - 1):
        return True

    for i in range(s - 1):
        x = pow(x, 2, n)
        if x == 1:
            return False
        elif x == n - 1:
            return True

    return False

def jacobi_symbol(a, n):
    """Calculate the Jacobi symbol (a/n)"""
    if n == 1:
        return 1
    elif a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        if n & 7 in [3, 5]:
            return -1
        elif n & 7 in [1, 7]:
            return 1
    elif a < 0:
        return (-1)**((n - 1) // 2) * jacobi_symbol(-1 * a, n)

    if not a & 1:
        return jacobi_symbol(2, n) * jacobi_symbol(a // 2, n)
    elif a % n != a:
        return jacobi_symbol(a % n, n)
    else:
        if a & 3 == n & 3 == 3:
            return -1 * jacobi_symbol(n, a)
        else:
            return jacobi_symbol(n, a)

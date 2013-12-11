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


def jacobi_symbol(a, n):
    """Calculate the Jacobi symbol (a/n)"""
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        if n % 8 in [3, 5]:
            return -1
        elif n % 8 in [1, 7]:
            return 1
    elif a < 0:
        return (-1)**((n-1)/2) * jacobi_symbol(-1*a, n)

    if a % 2 == 0:
        return jacobi_symbol(2, n) * jacobi_symbol(a / 2, n)
    elif a % n != a:
        return jacobi_symbol(a % n, n)
    else:
        if a % 4 == n % 4 == 3:
            return -1 * jacobi_symbol(n, a)
        else:
            return jacobi_symbol(n, a)

def lucas_pp(n, D):
    P = 1
    Q = (1 - D)/4                                                                                                                                                                                                                           

    def calculate_add_or_multiply(n):
        op_list = []
        while n != 1:
            if n % 2 == 0:
                op_list.append('*')
                n = n / 2
            else:
                op_list.append('+')
                n -= 1
        return reversed(op_list)

    def perform_operations(U, V, op_list):
        k = 1

        for operation in op_list:
            if operation == '*':
                U, V = U*V, V**2 - 2*(Q**k)
                k *= 2
            else:
                k += 1
                if (P*U + V) % 2 == 0:
                    if (D*U + P*V) % 2 == 0:
                        U, V = (P*U + V)/2, (D*U + P*V)/2
                    else:
                        U, V = (P*U + V)/2, (D*U + P*V + n)/2
                elif (D*U + P*V) % 2 == 0:
                    U, V = (P*U + V + n)/2, (D*U + P*V)/2
                else:
                    U, V = (P*U + V + n)/2, (D*U + P*V + n)/2
        return U, V

    U, V = perform_operations(1, P, calculate_add_or_multiply(n+1))

    if U % n != 0:
        return False # Failed the weaker probable prime test

    d = n + 1
    s = 0
    while d % 2 == 0:
        d = d/2
        s += 1

    U, V = perform_operations(1, P, calculate_add_or_multiply(d))

    if U % n == 0:
        return True # A strong probable prime

    for r in xrange(s):
        U, V = perform_operations(1, P, calculate_add_or_multiply(d*(2**r)))
        if V % n == 0:
            return True

    return False

def D_chooser(n):
    D = 5
    while jacobi_symbol(D, n) != -1:
        D += 2 if D > 0 else -2
        D *= -1
    return D

def baillie_psw(n):
    for x in [2, 3, 5, 7, 11, 13, 17, 19]:
        if n % x == 0 and n != x:
            return False
    if not miller_rabin_base_2(n):
        return False
    if not lucas_pp(n, D_chooser(n)):
        return False
    return True
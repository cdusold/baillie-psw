from baillie_psw import *
import time, argparse

order_2_primes = [101, 103, 107, 109, 113,
                    127, 131, 137, 139, 149]

order_3_primes = [1009, 1013, 1019, 1021, 1031, 
                    1033, 1039, 1049, 1051, 1061]

order_4_primes = [10007, 10009, 10037, 10039, 10061,
                    10067, 10069, 10079, 10091, 10093]

order_5_primes = [100003, 100019, 100043, 100049, 100057,
                    100069, 100103, 100109, 100129, 100151]

order_6_primes = [1000003, 1000033, 1000037, 1000039, 1000081,
                    1000099, 1000117, 1000121, 1000133, 1000151]

order_7_primes = [10000019, 10000079, 10000103, 10000121, 10000139,
                    10000141, 10000169, 10000189, 10000223, 10000229]


primes = {2: order_2_primes, 3: order_3_primes, 4: order_4_primes,
            5: order_5_primes, 6: order_6_primes, 7: order_7_primes}

def time_execution_primes(order):
    prime_list = primes[order]
    total_time = 0
    iterations = len(prime_list)
    for prime in prime_list:
        start_time = time.time()
        baillie_psw(prime)
        total_time += (time.time() - start_time)
    return total_time/iterations, iterations

def short_test():
    results = {}
    for order in [2, 3, 4, 5]:
        results[order] = time_execution_primes(order)
    return results

def medium_test():
    results = {}
    for order in [2, 3, 4, 5, 6]:
        results[order] = time_execution_primes(order)
    return results

def long_test():
    results = {}
    for order in [2, 3, 4, 5, 6, 7]:
        results[order] = time_execution_primes(order)
    return results

def process_results(results):
    for order, result in results.iteritems():
        print "Order {0}, average time: {1:f}s, number of iterations: {2}".format(order, *result)

parser = argparse.ArgumentParser(description='Test the Baillie-PSW implementation')
group = parser.add_mutually_exclusive_group()
group.add_argument('--short', help='Test primes up to order 5', action='store_true')
group.add_argument('--medium', help='Test primes up to order 6', action='store_true')
group.add_argument('--long', help='Test primes up to order 7', action='store_true')
args = parser.parse_args()

if args.short:
    results = short_test()
elif args.medium:
    results = medium_test()
elif args.long:
    results = long_test()

process_results(results)
from argparse import ArgumentParser

from baillie_psw import baillie_psw

parser = ArgumentParser(description='Check primality using Baillie-PSW')
parser.add_argument('number', help='Return whether number is prime', type=int)
args = parser.parse_args()

if args.number:
    print('Prime' if baillie_psw(args.number) else 'Composite')

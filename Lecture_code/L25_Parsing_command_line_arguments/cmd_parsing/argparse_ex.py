import argparse
description = 'Script for adding two numbers'
parser = argparse.ArgumentParser(description=description)

parser.add_argument('--a', help='First number', default=0, type=float)
parser.add_argument('--b', help='Second number', default=0, type=float)
# parser.add_argument('-m', '--method', help='Method what to do', type=str)
# parser.add_argument('--param', dest='p')
#parser.add_argument('counter')

group = parser.add_mutually_exclusive_group()
group.add_argument('--v', action='store_true')
group.add_argument('--q', action='store_true')

args = parser.parse_args()
print(args)
print(f"a: {type(args.a)} {args.a}")
print(f"b: {type(args.b)} {args.b}")
# print(args.p)
# print(args.param)

a = args.a
b = args.b

if args.v:
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"{a} + {b} = {a + b}")
elif args.q:
    print(a + b)
else:
   print(f"{a} + {b} = {a + b}")

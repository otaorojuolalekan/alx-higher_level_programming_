#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

nargs = len(argv) - 1

if nargs != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    quit(1)

op = argv[2]
if op != '+' and op != '-' and op != '*' and op != '/':
    print("Unknown operator. Available operators: +, -, * and /")
    quit(1)

a = int(argv[1])
b = int(argv[3])

if op == '+':
    result = add(a, b)
elif op == '-':
    result = sub(a, b)
elif op =='*':
    result = mul(a, b)
elif op == '/':
    result = div(a, b)

print("{} {} {} = {}".format(a, op, b, result))
quit(0)

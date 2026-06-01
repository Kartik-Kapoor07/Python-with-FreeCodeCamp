import argparse

parser=argparse.ArgumentParser()

parser.add_argument(
    "--Operation",
    choices=["add","sub","mul","div"],
    metavar="OPERATION",
    help="Choose the operation to perform 'add','sub','mul','div'")

parser.add_argument(
    "--num1",
    type=float,
    help="Enter the first number")

parser.add_argument(
    "--num2",
    type=float,
    help="Enter the second number")

args=parser.parse_args()

if args.Operation=="add":
    result=args.num1+args.num2
elif args.Operation=="sub":
    result=args.num1-args.num2
elif args.Operation=="mul":
    result=args.num1*args.num2
elif args.Operation=="div":
    result=args.num1/args.num2

print(result)# Update learning

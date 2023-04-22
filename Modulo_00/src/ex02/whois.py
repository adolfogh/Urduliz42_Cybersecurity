import sys

def check_number(num):
    if not isinstance(num, int):
        print("Error: Argument must be an integer.")
        return
    if num == 0:
        print("The number is zero.")
    elif num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

if len(sys.argv) == 1:
    print("Usage: python program_name.py <number>")
elif len(sys.argv) > 2:
    print("Error: Too many arguments.")
else:
    check_number(int(sys.argv[1]))
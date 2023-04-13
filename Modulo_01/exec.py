import sys

def reverse_swapcase(string):
    if string:
        string = ' '.join(string)
        print(string[::-1].swapcase())
    else:
        print('Usage: python exec.py <string>')
        
if __name__ == '__main__':
    reverse_swapcase(sys.argv[1:])
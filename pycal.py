import argparse

def equation(equation):
    try:
        return eval(args.equation)
    
    except NameError:
        return 'Please type a valid input'
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--equation', help = 'Returns the answer to an inputed equation')
    args = parser.parse_args()
    if args.equation:
        print(equation(args.equation))

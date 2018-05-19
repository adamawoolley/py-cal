input_error = 'Please enter a valid input'
options = '''
    There are currently 2 options
    1. Input an equation and get the answer
    2. Input mean followed by a list of numbers separated by spaces
    '''
def equation(equation):
    if '^' in equation:
        equation = str.replace(equation, '^', '**')

    try:
        return eval(equation)

    except:
        return input_error
    
def mean(numbers):
    mean = 0

    #removes white space from list
    for i in numbers[1:]:
        try:
            float(i)
        except:
            numbers.remove(i)

    for i in numbers[1:]:
        try:
            mean += float(i)
        except:
            return input_error
    try:
        return mean / (len(numbers) - 1)
    except:
        return input_error
    
if __name__ == "__main__":
    intro = '''
        Welcome to the python calculator.
        To use this simply type in the equation you want answered.
        To get a list of other uses type help.
        To exit type ctr-c or delete
        '''

    print(intro)

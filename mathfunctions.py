def equation(equation):
    if '^' in equation:
        equation = str.replace(equation, '^', '**')

        return eval(equation)
    
def mean(numbers):
    mean = 0

    for i in numbers:
        mean += float(i)

    return mean / (len(numbers) - 1)

def rt(squared, power, places):
  guess = squared
  while True:
      
    change = ((guess**power) -  squared)/(power*guess**(power - 1))
    guess -= change
    
    if (change < 10**(-places)):
      break
    
  return round(guess, places)

def prime(tested_number):
    
    number = 2
    prime = True

    while Prime == True and number < tested_number / 2:

        if tested_number % number == 0:
            prime = False
        else:
            number += 1
            
    if prime == False:
        return 0

    else:
        return 1

from mathfunctions import equation, mean, rt, prime

input_error = 'Please enter a valid input'
options = '''
Welcome to pycal!
If you need help, type help
    '''


if __name__ == "__main__":

    print(options)
    
    ans = 0

    while True:
        
        user_input = input('>>>')
        user_input = user_input.split(' ')

        for i in user_input:
            if 'ans' in i:
                user_input[user_input.index(i)] = ans
                
        try:
            if user_input[0] == 'mean':
                
                try:
                    ans = mean(user_input[1:])
                    print(ans)
                except:
                    print(input_error)

            elif user_input[1] == 'rt':
                
                try:
                    ans = rt(int(user_input[2]), int(user_input[0]), int(user_input[3]))
                    print(ans)
                except:
                    print(input_error)

#        elif user_input == 'prime':
#
#            for i in user_input[1:]:
#            
#                try:
#                    ans = prime(i)
#                    print(ans)
#                except:
#                    print(input_error)
                
        except:
            
            try:
                ans = equation(user_input)
                print(ans)
            except:
                print(input_error)

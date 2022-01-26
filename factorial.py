def factorial(n, init_num = 1):     # Creating a parameter init_num and setting equal to 1
    number = init_num      # Initialising an number variable that is equal to init_num
    if n == 1:      # n = 1 is the base case
        print(number)
    else:
        number = init_num * n       # The first run through the function is 1, init_num' multiplied by the parameter 'n'
        factorial(n-1,number,)      # Recursive call which edges to base case and take number as init_num parameter

factorial(8)
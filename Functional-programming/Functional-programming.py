# 1
def factorial(n):
    if n < 2:
        return 1
    return n*factorial(n-1)


# 2
def is_prime(n):
    if n < 2:
        return False
    potential_dividers = [i for i in range(2,int(n**0.5) + 1)]
    return all(n % x != 0 for x in potential_dividers)

# 3
def filter_odd(numbers):
    return list(filter(lambda x: x % 2 == 1, numbers))


# 4
def map_square(numbers):
    return list(map(lambda x: x**2, numbers))


# 5
from functools import reduce
def reduce_sum(numbers):
    return reduce(lambda x,y: x + y, numbers)

# 6
def partial_apply(func):
    partial_func = lambda x: func(x)
    return partial_func

# 7
def compose(f,g):
    h = lambda x: g(f(x))
    return h

# 8
def create_function_with_arguments(func,arguments):
    def new_func():
        return func(arguments)
    return new_func()

# 9 поочередное применение функций из списка 
def compose_functions(functions):

    def composed_function(arg,ind = 0): #проходимся вместо цикла рекурсией
        if ind == len(functions) - 1:
            return functions[ind](arg)
        return composed_function(functions[ind](arg),ind + 1)
    
    return composed_function
functions = [lambda x:x+1, lambda x: x+2, lambda x: x + 3]
print(compose_functions(functions)(10)) #10 -> 11 -> 13 ->16
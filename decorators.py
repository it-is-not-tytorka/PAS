import time
def my_decorator_timer(func):
    def inside_func(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        return time.time() - start
    return inside_func

def my_decorator_cache(func):
    dict_of_values = dict()
    def inside_func(x):
        if x not in dict_of_values:
            dict_of_values[x] = func(x)
        return dict_of_values[x]
    return inside_func

# на проверку (спасибо вам за прекрасные код-ревью :) )
# кстати, заметил, что если вызывать этот декратор как @ перед функцией, которая использует в себе рекурсию, например:
# @my_decorator_logging
# def fact(n):
#   if n < 2:
#       return 1
#   return n*fact(n-1)
# то программа не будет работать, потому что она будет вызывать себя fact(n-1) снова с декоратором, а декоратор не дает
# подсчитать значение, он выполняет другую работу, в таких случаях работает просто my_decorator_logging(fact)(n)
def my_decorator_logging(func):
    def inside_func(*args,**kwargs):
        with open('my_log.log','a') as file:
            result = func(*args,**kwargs)
            file.write(f'Функция {func.__name__} делает брбрбр {result}\n')
    return inside_func

def my_decorator_retry(func,retries,retry_time):
    def inside_func(*args,**kwargs):
        for i in range(retries):
            if func(*args,**kwargs) != None:
                break
            else:
                time.sleep(retry_time)
    return inside_func



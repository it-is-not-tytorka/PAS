def sum_numbers(*args):
    return sum(number for number in args)

def print_kwargs(**kwargs):
    for key in kwargs:
        print(f'{key}: {kwargs[key]}')

def filter_by_length(min_length, *args):
    filtered_lines = []
    for line in args:
        if len(line) >= min_length:
            filtered_lines.append(line)
    return filtered_lines

def calculate_total_price(price,**kwargs):
    discount = 0
    for key in kwargs:
        discount += kwargs[key]
    return price*(1 - discount/100)

def custom_print(*args,**kwargs):
    answer = ''
    separation = ' '
    end_of_print = '\n'
    if 'end' in kwargs.keys() or 'sep' in kwargs.keys():
        for key in kwargs:
            if key == 'sep':
                separation = kwargs[key]
            if key == 'end':
                end_of_print = kwargs[key]
    for element in args:
        answer += str(element)
        if element != args[-1]:
            answer += separation
    print(answer + end_of_print)

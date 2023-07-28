# 1
# 1 код - ООП, так как создаются новые классы и методы, которые к ним применяются
# 2 код - функциональное программирование, так как все действия происходят в функциях, не используется
# циклы, функции можно заменить на значение, которые они выводят
# 3 код - императивное, так как все действия происходят шаг за шагом, используются циклы

# 2
def sum_even_numbers(numbers):
    answer = sum(map(lambda x: x if x % 2 == 0 else 0, numbers))
    return answer

numbers = [14, 93, 19, 38, 18, 51, 77]
print(sum_even_numbers(numbers))

# 3
def sum_even_numbers(numbers):
    answer = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            answer += numbers[i]
    return answer

numbers = [60, 84, 9, 49, 7, 85, 38]
print(sum_even_numbers(numbers))
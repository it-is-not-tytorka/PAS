from functools import reduce

L1 =  [2, 4, 6, 8, 0, 3, 4, 2, 3, 5, 1, 2]
# x**2 % 9 == 0 <=> x % 3 == 0
# 1 получаем список, в котором остается выбрать максимум и не париться
a_filtered = list(filter(lambda x: x % 3 == 0, L1))
maxim = reduce(lambda x,y: x if x > y else y, a_filtered)
# 2 делаем в одну строчку, но очень сильно стараемся избежать чисел, которые не делятся на 3
answer = reduce(lambda x,y: y if (y % 3 == 0) and (y > x - 10000000000000*(x % 3 != 0)) else x - 10000000000*(x % 3 != 0), L1)
print(maxim,answer)
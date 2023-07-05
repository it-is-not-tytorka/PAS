a = (y +' '+ x for x in ['Крести','Пики','Черви','Бубны'] for y in ['6','7','8','9','10','Валет','Дама','Король','Туз'])
iterator = iter(a)

while True:
    try:
        print(next(iterator))
    except StopIteration: # тут можно было как угодно: хоть range(36), чтобы перебрать все элементы, но мне этот вариант понравился
        print('Stop iteration')
        break


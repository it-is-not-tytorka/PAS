# 1
s = input().split()
try:
    print(int(s[0])/int(s[-1]))
except ZeroDivisionError:
    print('ERROR')

# 2
rows = []
while True:
    x = input()
    if x != '':
        rows.append(x)
    else:
        break
passwords = []
for x in rows:
    try:
        int(x,16)
        passwords.append(x)
    except ValueError:
        pass
print(passwords)

# 3

def are_you_winning_son(name_of_participant,olymp1,olymp2):
    answer = f'[{olymp1["name"]}] '
    try:
        answer += f"{olymp1['winners'][name_of_participant]}\n"
    except KeyError:
        answer += '\n'
    answer += f'--------------------\n'

    answer += f'[{olymp2["name"]}] '
    try:
        answer += f"{olymp2['winners'][name_of_participant][4]}\n"
    except (KeyError,IndexError):
        answer += '\n'
    answer += f"--------------------\n"
    return answer

olympiad1 = {"name": "Пробная вышка",
    "winners": {
        "Олеся Олимпиадникова": 594,
        "Олег Олимпиадников": 587,
        "Онисим Олимпиадников": 581,
        }
    }

olympiad2 = {"name": "Горные воробьи",
    "winners": {
        "Ольга Олимпиадникова": (20, 20, 19, 20),
        "Олеся Олимпиадникова": (19, 19, 20, 20, 17),
        "Офелия Олимпиадникова": (20, 20, 20, 20, 13)
        }
    }

print(are_you_winning_son('Ольга Олимпиадникова',olympiad1,olympiad2))
print(are_you_winning_son('Олеся Олимпиадникова',olympiad1,olympiad2))
assert len(olympiad2['winners']['Ольга Олимпиадникова']) == 5,'Баллы за пятую задачу не выставили'

# 4
try:
    while True:
        pass
except:
    while True:
        pass

# 5
class Animal_in_glass(Exception):
    pass
class Question(Exception):
    pass

try:
    count_of_glasses = input('Сколько кружек лимонада вы бы хотели?')
    if count_of_glasses == 'ящерица':
        raise Animal_in_glass
    if count_of_glasses.startswith('где'):
        raise Question
    count_of_glasses = int(count_of_glasses)
    assert count_of_glasses > 0 and count_of_glasses < 100
except AssertionError:
    print('Извините, но вы ввели слишком много или мало кружек')
except ValueError:
    print('Извините, мы можем налить только целое количество кружек')
except Animal_in_glass:
    print('Ящериц не наливаем')
except Question:
    print('Бар сгроел')
else:
    print(f'Вы заказали корректное количество кружек: {count_of_glasses}')
    print('Спасибо!')
finally:
    print('Приходите к нам еще')
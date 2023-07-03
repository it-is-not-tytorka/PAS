import copy
import sys

# backpack = ['capybara','capyraba','capyba','capyba','capybara',2999,2999,'capybara',[7,7,7],[7,7,7],[7,7,7],[7,7,7]] + [[8,8]]*5
# print(backpack)
# ans_is = 0
# ans_eq = 0
# for i in range(len(backpack)):
#     for j in range(i+1,len(backpack)):
#         if backpack[i] is backpack[j]:
#             ans_is +=1
#         if backpack[i] == backpack[j]:
#             ans_eq += 1
# print(ans_is)
# print(ans_eq)


rec_salad = ['lettuce','chicken','cheese','sauce','tomatoes','croutons']
rec_salad.append(rec_salad)
#насколько я понял, обращение в данном случае означает количество раз, когда мы зашли в рекурсивный салат, т.е. rec_salad - 1 обращение, rec_salad[6] - 2 обращение, так как мы зашли на уровень глубже, rec_salad[6][6] - 3 и т д
rec_salad[6].append('salt')
rec_salad[6].append('pepper')
ans = rec_salad #это первое обращение, в цикле ниже делаем еще 126 обращений, т.е. в итоге мы получим как раз 127 обращение
for i in range(126):
    ans = ans[6]
print(ans[4],rec_salad[6][-1]) #ответ tomatoes peppper
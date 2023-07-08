# def f1(file_name):
#     with open(f'{file_name}','r') as file:
#         row = ''
#         for line in file:
#             row += line.rstrip()
#         return row
#
#
# def f2(file_name):
#     with open(f'{file_name}') as file:
#         return file.readline()
#
#
# def f3(file_name):
#     with open(f'{file_name}') as file:
#         return file.readlines()
#
#
# def f4(file_name):
#     with open(f'{file_name}') as file:
#         lines_without_slash_n = []
#         for line in file:
#             lines_without_slash_n.append(line.rstrip())
#         return lines_without_slash_n
#
#
# def f5(file_name):
#     with open(f'{file_name}') as file:
#         lines = ''
#         for line in file:
#             lines += line
#         return lines


def f6(file_name):
    with open(f'{file_name}') as file:
        all_lines_with_space = ''
        for line in file:
            all_lines_with_space += line.rstrip() + ' '
        return all_lines_with_space


# def f7(line):
#     return line.rstrip()


def f8(line):
    return line.rstrip('!?.')
print(f8('what!......????!!?!?!?!??!......'))


# def f9(file_name, variable):
#     with open(f'{file_name}','a') as file:
#         file.write(variable)
# f9('input.txt','mamaaaaaaaaa yyyyyyyyyyoyoooooooooo')
#
# def f10(file_name,variable):
#     with open(f'{file_name}','a') as file:
#         file.write(f'{variable}\n')
# f10('input.txt','life just had beguuun')
#
# def f11(file_name,List1):
#     with open(f'{file_name}','a') as file:
#         for line in List1:
#             file.write(line)
# f11('input.txt', ['but now',"i'm gone", 'and throuwn it all', 'awaayyyy'])
#
# def f12(file1_name,file2_name):
#     with open(f'{file1_name}','r') as file_read:
#         with open(f'{file2_name}','a') as file_append:
#             for line in file_read:
#                 print(line.rstrip(),file = file_append)
#
#
# def f13(file1_name,file2_name):
#     with open(f'{file1_name}','r') as file_read:
#         with open(f'{file2_name}','a') as file_append:
#             for line in file_read:
#                 if line.startswith('hello') and line.endswith('world'):
#                     file_append.write(line)

def f14(file_name):
    dictionary_answer = {}
    with open(f'{file_name}','r',encoding='utf-8') as file:
        name_ind = None
        pet_ind = None
        age_of_pet_ind = None
        for line in file:
            line_list = line.split()
            if name_ind == None or pet_ind == None or age_of_pet_ind == None: # первый пробег line по файлу будет нахоить индексы имён и прочего, это позволяет алгоритму работать даже если мы не будем знать, как слова расположены в заголовке
                for i in range(len(line_list)):
                    if line_list[i] == 'Имя':
                        name_ind = i
                    if line_list[i] == 'Питомец':
                        pet_ind = i
                    if line_list[i] == 'Возраст_питомца':
                        age_of_pet_ind = i
            else:
                dictionary_answer[line_list[name_ind]] = {}
                dictionary_answer[line_list[name_ind]][line_list[pet_ind]] = line_list[age_of_pet_ind]
    return dictionary_answer
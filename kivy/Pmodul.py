from random import choice

def decoder(library, k, word_2, file):
    '''Преобразовывает входящее значение в соответсвующий библиотеке символ'''
    a = file.read(k) # читает первые k символа(-ов)
    with open(library, "r", encoding='utf-8') as file_lib:
        for line in file_lib:
            #line = line.replace("\n", "")
            split_line = line.split(", ")
            if a in split_line:
                a = split_line[0]
                word_2.append(a)
                break

def coder(library, a, file):
    '''Преобразовывает входящий символ в кодовое слово, взятое из библиотеки'''
    with open(library, "r", encoding='utf-8') as file_lib:
        for line in file_lib:
            #line = line.replace("\n", "")
            split_line = line.split(", ")
            if a in split_line:
                a = choice(split_line[1:])
                file.write(a)
                break

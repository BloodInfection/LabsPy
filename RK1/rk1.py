# Филатова Анастасия ИУ5-55Б
# Запрос Д
# Предметная область 22 - Библиотека и Язык программирования
from operator import itemgetter

class Library:
    # Библиотека
    def __init__(self, id, title, number, pl_id):
        self.id = id
        self.title = title
        # number - любое произвольное число, так как по заданию рк необходимо любое числовое значение
        self.number = number
        self.pl_id = pl_id

class Programming_language:
    # Язык программирования
    def __init__(self, id, name):
        self.id = id
        self.name = name

class LibrProg_lan:
    # Операторы языка программирования
    # для реализации связи многие-ко-многим
    def __init__(self, progLan_id, libr_id):
        self.progLan_id = progLan_id
        self.libr_id = libr_id

# Языки программирования
progLang = [
    Programming_language(1, "Basic"),
    Programming_language(2, "Pascal"),
    Programming_language(3, "C++"),
    Programming_language(4, "Python"),
    Programming_language(5, "Java"),
    Programming_language(6, "C#")
]

# операторы
libr = [
    Library(1, "String", 17, 1),
    Library(2, "Twig", 50, 2),
    Library(3, "Int", 22, 2),
    Library(4, "Double", 14, 3),
    Library(5, "Queue", 38, 3),
    Library(6, "Numpy", 32, 3),
    Library(7, "Vector", 28, 3)
]

libr_progLang = [
    LibrProg_lan(1, 1),
    LibrProg_lan(2, 2),
    LibrProg_lan(2, 3),
    LibrProg_lan(3, 4),
    LibrProg_lan(3, 5),
    LibrProg_lan(3, 6),
    LibrProg_lan(3, 7),

    LibrProg_lan(4, 1),
    LibrProg_lan(4, 2),
    LibrProg_lan(4, 3),
    LibrProg_lan(5, 4),
    LibrProg_lan(6, 5),
    LibrProg_lan(6, 6),
    LibrProg_lan(6, 7),
]

def main():
    # соединение данных один-ко-многим
    one_to_many = [(c.title, c.number, o.name)
                   for o in progLang
                   for c in libr
                   if c.pl_id == o.id]

    # соединение данных многие-ко-многим
    many_to_many_temp = [(o.name, co.progLan_id, co.libr_id)
                         for o in progLang
                         for co in libr_progLang
                         if o.id == co.progLan_id]

    many_to_many = [(c.title, c.number, pl_name)
                    for pl_name, progLan_id, oper_id in many_to_many_temp
                    for c in libr if c.id == oper_id]

    print('Задание Д1')
    res1 = []
    for o in one_to_many:
        if o[0][-1:] == "g":
            res1.append(o[0:3:2])
    print(res1)

    print('\nЗадание Д2')
    res2_unsorted = []
    for o in progLang:
        o_oper = list(filter(lambda i: i[2] == o.name, one_to_many))
        if len(o_oper) > 0:
            o_number = [number for _, number, _ in o_oper]
            o_number_sum = sum(o_number)
            o_number_count = len(o_number)
            o_number_average = o_number_sum / o_number_count
            res2_unsorted.append((o.name, int(o_number_average)))
    res2 = sorted(res2_unsorted, key=itemgetter(1), reverse=True)
    print(res2)

    print('\nЗадание Д3')
    res3 = {}
    for o in progLang:
        if o.name[0] == "P":
            o_oper = list(filter(lambda i: i[2] == o.name, many_to_many))
            o_oper_titles = [x for x, _, _ in o_oper]
            res3[o.name] = o_oper_titles
    print(res3)


if __name__ == '__main__':
    main()
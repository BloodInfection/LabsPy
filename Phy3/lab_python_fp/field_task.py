# Пример:
goods = [
    {'title': 'Ковер', 'price': '2000', 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': '5300', 'color': 'black'},
    {'title': 'Кровать', 'price': '10500', 'color': 'white'}
]


def field(items, *args):
    assert len(args) > 0, 'Не переданы аргументы полей словаря'
    count = 0
    if len(args) == 1:
      for i in items:
        count += 1
        print('\'', end='')
        print(i.get(*args), end='')
        if count < len(items):
          print('\'', end=', ')
        else:
         print('\'')
    else:
      for i in items:
        count += 1
        k = 0
        print('{\'', end='')
        while k < len(args):
          temp_args = args[k]
          k += 1
          print(temp_args, end='')
          print('\': \'', end='')
          print(i.get(temp_args), end='')
          if k < len(args):
            print('\', \'', end='')
          else:
            print('\'', end='')
        if count < len(items):
          print('}, ', end='')
        else:
          print('}')


def main():
    #field(goods)
    field(goods, 'title')
    field(goods, 'title', 'price')
    field(goods, 'title', 'price', 'color')


if __name__ == "__main__":
    main()

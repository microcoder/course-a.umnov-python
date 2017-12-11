import argparse

def count_lines(filename):
    "Подсчитывает количество строк в файле"
    with open(filename) as f:
        count = 0
        for line in f:
            count += 1
    return count

def count_symbols(filename, line_index):
    "Подсчитывает количество символов в указанной строке аргументом line_index"
    with open(filename) as f:
        current = 0
        for line in f:
            if current == line_index:
                return len(line) -1
            current += 1


def main():
    """Если вызвать скрипт без аргументов, то argparse автоматически выведет ошибку.
    Если вызвать скрипт с аргументом -h, то argparser выведет справку.

    Пример вызова: python3 script_argparse.py -l 1 test.txt
    """

    # Создается экземпляр парсера
    parser = argparse.ArgumentParser()

    # Добавляется порядковый аргумент (без черточек), с обязательным значением
    parser.add_argument('filename', help='name of input file')

    # Добавляется именованный аргумент (с черточками), с необязательным значением (default=None)
    parser.add_argument('-l', '--line', type=int, default=None, help='count symbols in line')

    # Еще можно добавить описание которое будет выводится в помощи над всеми аргументами после строчки 'usage'
    parser.description = (
            'Lines and symbol counting '
            'utilities.')

    # Можно еще приравнять описание к докстрингу этого модуля
    # parser.description = __doc__

    # Следующей командой парсятся аргументы из sys.argv где ожидается обязательный аргумент 'filename',
    # если аргумент не находится, то происходит Exception с выводом справки
    args = parser.parse_args()

    if args.line is None: # Если у переданного аргумента line отсуствует значение
        print(count_lines(args.filename))
    else:
        # Выполняется, если аргумент filename и --line переданы этому скрипту:
        print(count_symbols(args.filename, args.line))

# Если скрипт/модуль вызывается напрямую, не через import
if __name__ == '__main__':
    main()

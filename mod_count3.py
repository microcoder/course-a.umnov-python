import sys

def count_lines(filename):
    with open(filename) as f:
        count = 0
        for line in f:
            count += 1
    return count

# Запускаем код только тогда, когда этот модуль является главным, т.е. его не импортировали в другой модуль
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Not enough arguments.')
    else:
        print(count_lines(sys.argv[1]))

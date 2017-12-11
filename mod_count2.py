import sys

def count_lines(filename):
    with open(filename) as f:
        count = 0
        for line in f:
            count += 1
    return count

if len(sys.argv) == 1 or len(sys.argv) > 2:
    print('Not enough arguments.')
else:
    print(count_lines(sys.argv[1]))

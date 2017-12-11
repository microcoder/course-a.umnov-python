def count_lines(filename):
    with open(filename) as f:
        count = 0
        for line in f:
            count += 1
    return count

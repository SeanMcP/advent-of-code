from utils.file import read_file

lines = read_file('2020/assets/expense_report.txt')

# PART 1
for i, val1 in enumerate(lines):
    product = None
    for j, val2 in enumerate(lines[i + 1:]):
        if val1 + val2 == 2020:
            product = val1 * val2
            break
    if product != None:
        print('Part 1 product:', product)
        break

# PART 2
for i, val1 in enumerate(lines):
    product = None
    for j, val2 in enumerate(lines[i + 1:]):
        for k, val3 in enumerate(lines[j + 1:]):
            if val1 + val2 + val3 == 2020:
                product = val1 * val2 * val3
                break
    if product != None:
        print('Part 2 product:', product)
        break

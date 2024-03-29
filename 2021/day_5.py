from utils.file import read_file

input = read_file('2021/assets/hydrothermal_venture.txt')

def to_int_list(ls):
    return list(map(lambda str: int(str), ls))

def to_coordinates(ln):
    output = ln.split(' -> ')
    first = to_int_list(output[0].split(','))
    second = to_int_list(output[1].split(','))
    return [first, second]

input = list(map(to_coordinates, input))

grid = dict()
greater_than_two = []

def sort_set(set):
    if set[0][0] < set[1][0]:
        return set
    else:
        return [set[1], set[0]]

def get_range(a, b):
    return range(a if a < b else b, (b if a < b else a) + 1)

def get_coord(x, y):
    return str(x) + ',' + str(y)

for set in input:
    # Diagonal segments
    if set[0][0] != set[1][0] and set[0][1] != set[1][1]:
        sorted = sort_set(set)
        multiplier = 1 if sorted[0][1] < sorted[1][1] else -1
        for i, x in enumerate(get_range(sorted[0][0], sorted[1][0])):
            coord = get_coord(x, sorted[0][1] + i * multiplier)
            if coord in grid:
                grid[coord] = grid[coord] + 1
                if grid[coord] == 2:
                    greater_than_two.append(coord)
            else:
                grid[coord] = 1

    if set[0][0] == set[1][0]:
        # Iterate y
        for y in get_range(set[0][1], set[1][1]):
            coord = get_coord(set[0][0], y)
            if coord in grid:
                grid[coord] = grid[coord] + 1
                if grid[coord] == 2:
                    greater_than_two.append(coord)
            else:
                grid[coord] = 1
    elif set[0][1] == set[1][1]:
        # Iterate x
        for x in get_range(set[0][0], set[1][0]):
            coord = get_coord(x, set[0][1])
            if coord in grid:
                grid[coord] = grid[coord] + 1
                if grid[coord] == 2:
                    greater_than_two.append(coord)
            else:
                grid[coord] = 1

# print('part 1:', len(greater_than_two))
print('part 2:', len(greater_than_two))
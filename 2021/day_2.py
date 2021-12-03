from utils.file import read_file

dive = read_file('2021/assets/dive.txt')

horizontal = 0
depth = 0
aim = 0

# Not sure why I need the _ here
# for _, line in enumerate(dive):
#     i = line.index(' ')
#     command = line[0:i]
#     value = int(line[i:])

#     if command == 'forward':
#         horizontal += value
#     elif command == 'backward':
#         horizontal -= value
#     elif command == 'up':
#         depth -= value
#     elif command == 'down':
#         depth += value

# print('part 1:', horizontal * depth)

# Not sure why I need the _ here
for _, line in enumerate(dive):
    i = line.index(' ')
    command = line[0:i]
    value = int(line[i:])

    if command == 'forward':
        horizontal += value
        depth += value * aim
    elif command == 'up':
        # depth -= value
        aim -= value
    elif command == 'down':
        # depth += value
        aim += value

print('part 2:', horizontal * depth)

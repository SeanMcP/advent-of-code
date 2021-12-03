from utils.file import read_file

sonar_sweep = read_file('2021/assets/sonar_sweep.txt', True)

increase_count = 0

for i, line in enumerate(sonar_sweep):
    if sonar_sweep[i - 1] and sonar_sweep[i - 1] < line:
        increase_count += 1

print('part 1:', increase_count)

increase_window_count = 0
windows = []

for i, line in enumerate(sonar_sweep):
    for j in range(0, 3):
        index = i - j
        if index < 0:
            continue
        if index > len(sonar_sweep):
            break
        if index < len(windows):
            windows[index].append(line)
            if len(windows[index]) == 3:
                sum = windows[index][0] + windows[index][1] + windows[index][2]
                windows[index] = sum
        else:
            windows.append([line])

# Not proud of this part, but I'm having trouble
# working with lists in Python
length = len(windows)
penultimate = length - 2
ultimate = length - 1

windows[penultimate] = windows[penultimate][0] + windows[penultimate][1]
windows[ultimate] = windows[ultimate][0]

for i, sum in enumerate(windows):
    if i - 1 > 0 and windows[i - 1] < sum:
        increase_window_count += 1

print('part 2:', increase_window_count)

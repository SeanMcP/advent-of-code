from utils.file import read_file

input = read_file('2021/assets/lanternfish.txt')
input = list(map(lambda str: int(str), input[0].split(',')))

class Fish:
    def __init__(self, starting_days = 8):
        self.days = starting_days
    
    def age(self):
        if self.days > 0:
            self.days -= 1
            return False
        else:
            # Time to spawn!
            self.days = 6
            return True

lanternfish = []

for i in input:
    lanternfish.append(Fish(i))

for day in range(0, 80):
    pending_count = 0
    for lf in lanternfish:
        if lf.age() == True:
            pending_count += 1
    for i in range(0, pending_count):
        lanternfish.append(Fish())

print('part 1:', len(lanternfish))
from utils.file import read_file

binary_diagnostic = read_file('2021/assets/binary_diagnostic.txt')

# gamma_rate = ''
# epsilon_rate = ''

# for i in range(0, len(binary_diagnostic[0])):
#     count1 = 0
#     count0 = 0
#     for binary in binary_diagnostic:
#         if binary[i] == '1':
#             count1 += 1
#         else:
#             count0 += 1
#     if count0 > count1:
#         gamma_rate += '0'
#     else:
#         gamma_rate += '1'

# def complimentGamma():
#     output = ''
#     for i in range(0, len(gamma_rate)):
#         if gamma_rate[i] == '0':
#             output += '1'
#         else:
#             output += '0'
#     return output

# epsilon_rate = complimentGamma()

# print('part 1:', int(gamma_rate, 2) * int(epsilon_rate, 2))

o_list = binary_diagnostic

for i in range(0, len(binary_diagnostic[0])):
    list_0 = []
    list_1 = []

    for binary in o_list:
        if binary[i] == '1':
            list_1.append(binary)
        else:
            list_0.append(binary)

    if len(list_0) > len(list_1):
        o_list = list_0
    else:
        o_list = list_1 # Flip this for C02

print('oxygen generator rating', o_list)

co2_list = binary_diagnostic

for i in range(0, len(binary_diagnostic[0])):
    list_0 = []
    list_1 = []

    if len(co2_list) == 1:
        break

    for binary in co2_list:
        if binary[i] == '1':
            list_1.append(binary)
        else:
            list_0.append(binary)

    if len(list_0) > len(list_1):
        co2_list = list_1
    else:
        co2_list = list_0

print('CO2 scrubber rating', co2_list)

print('part 2:', int(o_list[0], 2) * int(co2_list[0], 2))
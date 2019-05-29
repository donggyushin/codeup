decimal = int(input())
hex = ''
hex_list = ['0', '1', '2', '3', '4', '5', '6',
            '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
while decimal > 0:
    rest = int(decimal % 16)
    hex = hex_list[rest] + hex
    decimal = int(decimal / 16)
print(hex)

hex = input()
hex_item = ['0', '1', '2', '3', '4', '5', '6',
            '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
decimal = 0
octal = ''
hex_list = []
for c in hex:
    hex_list.append(c)
hex_list = hex_list[::-1]
i = 1
for c in hex_list:
    decimal = decimal + hex_item.index(c) * i
    i = i * 16
while decimal > 0:
    rest = str(int(decimal % 8))
    octal = rest + octal
    decimal = int(decimal / 8)
print(octal)

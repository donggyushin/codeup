octal = str(int(input()))
octal_list = []
decimal = 0
for c in octal:
    octal_list.append(c)
octal_list = octal_list[::-1]
i = 1
for list_item in octal_list:
    decimal = decimal + int(list_item) * i
    i = i * 8
print(decimal)

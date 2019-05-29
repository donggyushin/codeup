decimal = int(input())
octal = ''
while decimal > 0:
    rest = decimal % 8
    rest = int(rest)
    rest = str(rest)
    octal = rest + octal
    decimal = int(decimal / 8)
print(octal)

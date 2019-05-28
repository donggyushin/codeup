number = int(input())
million = str(number/10000 * 10000)
thousand = str(number % 10000/1000 * 1000)
hundred = str(number % 1000/100 * 100)
ten = str(number % 100/10 * 10)
one = str(number % 10)
numbers = [million, thousand, hundred, ten, one]
for n in numbers:
    print('['+n+']')

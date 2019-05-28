def print_three_times(x):
    for _ in range(3):
        print(x, end=' ', flush=True)


if __name__ == '__main__':
    num = int(input())
    print_three_times(num)

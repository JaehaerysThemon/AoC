def find_make(signal, length=4):
    for i in range(length, len(signal)):
        if len(set(signal[i-length:i])) == length:
            return i


if __name__ == '__main__':
    with open('./input/day-06.ipt', 'r') as file:
        line = file.readline()

    print(find_make(line))
    print(find_make(line,14))

def find_2020(path):
    with open(path, 'r') as file:
        prev = []
        for num in file:
            if 2020 - int(num) in prev:
                return int(num) * (2020 - int(num))
            prev.append(int(num))


def find_x(x, numbers):
    prev = []
    for num in numbers:
        if x-num in prev:
            return [num, x-num]
        prev.append(num)
    return False


def find_2020_3(path):
    with open(path, 'r') as file:
        prev = []
        for num in file:
            num = int(num)
            if find_x(2020-num, prev):
                [x1, x2] = find_x(2020-num, prev)
                return num * x1 * x2
            prev.append(num)


if __name__ == '__main__':
    print(find_2020('./input/day-01.ipt'))
    print(find_2020_3('./input/day-01.ipt'))

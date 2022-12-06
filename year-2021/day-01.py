def sub_depth(measurements, space = 1 ):
    counter = 0
    for i in range(space, len(measurements)):
        counter += 1 if measurements[i] - measurements[i-space] > 0 else 0
    return counter


if __name__ == '__main__':
    lines = []
    with open('./input/day-01.ipt', 'r') as file:
        for line in file:
            lines.append(int(line))
    print(sub_depth(lines))
    print(sub_depth(lines, 3))

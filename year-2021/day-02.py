def sub_direction(directions, amounts):
    horizontal, depth = 0, 0
    for (direction, amount) in zip(directions, amounts ):
        if direction == 'f':
            horizontal += amount
        else:
            depth += amount * direction
    return horizontal * depth


def sub_forwards(directions, amounts):
    horizontal, depth, aim = 0, 0, 0
    for (direction, amount) in zip(directions, amounts ):
        if direction == 'f':
            horizontal += amount
            depth += amount * aim
        else:
            aim += direction * amount
    return horizontal * depth

if __name__ == '__main__':
    lines = []
    values = []
    with open('./input/day-02.ipt', 'r') as file:
        for line in file:
            values.append(int(line[-2]))
            if line[0] == 'u':
                lines.append(-1)
            elif line[0] == 'd':
                lines.append(1)
            else:
                lines.append(line[0])

    print(sub_direction(lines, values))
    print(sub_forwards(lines, values))

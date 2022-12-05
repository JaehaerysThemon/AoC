def find_duplicates(rucksacks):
    score = 0
    for rucksack in rucksacks:
        half_len = int(len(rucksack[:-1])/2)
        first, last = set(rucksack[:half_len]), set(rucksack[half_len:-1])
        duplicate = list(first.intersection(last))[0]
        score += (ord(duplicate) - 38) if duplicate.isupper() else ord(duplicate) - 96

    return score


def find_badge(rucksacks):
    score = 0
    group = []
    for rucksack in rucksacks:
        if len(group) < 3:
            group.append(set(rucksack[:-1]))
        if len(group) == 3:
            int_0_1 = group[0].intersection(group[1])
            badge = list(group[2].intersection(int_0_1))[0]
            score += (ord(badge) - 38) if badge.isupper() else ord(badge) - 96
            group = []
    return score


if __name__ == '__main__':
    with open('./input/day-01.ipt', 'r') as file:
        print(find_duplicates(file))
    with open('./input/day-01.ipt', 'r') as file:
        print(find_badge(file))

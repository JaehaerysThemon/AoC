def find_duplicates(rucksacks):
    score = 0
    for rucksack in rucksacks:
        half_len = int(len(rucksack[:-1])/2)
        first, last = set(rucksack[:half_len]), set(rucksack[half_len:-1])
        duplicate = list(first.intersection(last))[0]
        score += (ord(duplicate) - 38) if duplicate.isupper() else ord(duplicate) - 96

    return score


def find_badge(rucksacks):
    pass


if __name__ == '__main__':
    with open('./input/day-01.ipt', 'r') as file:
        print(find_duplicates(file))
    with open('./input/day-01.ipt', 'r') as file:
        print(find_badge(file))

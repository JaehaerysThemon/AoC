def find_containing_shifts(shift_pairs):
    overlaps = 0
    for shift_pair in shift_pairs:
        [shift_1, shift_2] = [pair.split('-') for pair in shift_pair[:-1].split(',')]
        shift_1, shift_2 = list(map(int, shift_1)), list(map(int, shift_2))
        if shift_1[0] >= shift_2[0] and shift_1[1] <= shift_2[1] or shift_1[0] <= shift_2[0] and shift_1[1] >= shift_2[1]:
            overlaps += 1
    return overlaps


def find_overlapping_shifts(shift_pairs):
    overlaps = 0
    for shift_pair in shift_pairs:
        [shift_1, shift_2] = [pair.split('-') for pair in shift_pair[:-1].split(',')]
        shift_1, shift_2 = list(map(int, shift_1)), list(map(int, shift_2))
        if shift_1[0] >= shift_2[0] and shift_1[0] <= shift_2[1] or shift_2[0] >= shift_1[0] and shift_2[0] <= shift_1[1]:
            overlaps += 1
    return overlaps


if __name__ == '__main__':
    with open('input', 'r') as file:
        print(find_containing_shifts(file))
    with open('input', 'r') as file:
        print(find_overlapping_shifts(file))

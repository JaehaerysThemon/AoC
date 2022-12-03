def jolt_difference(adapters_file):
    adapters = []
    for adapter in adapters_file:
        adapters.append(int(adapter))
    adapters.sort()
    diffs = [adapters[0]]
    for i in range(1, len(adapters)):
        diffs.append(adapters[i]-adapters[i-1])
    print(diffs)
    jolt_1_diff = diffs.count(1)
    jolt_3_diff = 1 + diffs.count(3)
    return jolt_1_diff * jolt_3_diff

def jolt_arrangements(adapters_file):
    adapters = []
    for adapter in adapters_file:
        adapters.append(int(adapter))
    adapters.sort()
    print(adapters)
    diffs = []
    j = 1
    for i in range(1, len(adapters)):
        diff = adapters[i]-adapters[i-1]
        if diff > 1:
            diffs.append(j)
            j = 0
        else:
            j += 1
    print(diffs)
    arrangements = 2
    for diff in diffs:
        if diff == 1:
            arrangements *= 1
        elif diff == 2:
            arrangements *= 4
        elif diff == 3:
            arrangements *= 7
        elif diff == 4:
            arrangements *= 13
    return arrangements



if __name__ == '__main__':
    with open('./input', 'r') as file:
        print(jolt_difference(file))
    with open('./input', 'r') as file:
        print(jolt_arrangements(file))

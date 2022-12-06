def binary_min_finder(nums):
    binary_ones = [0 for j in range(len(nums[0]))]
    for num in nums:
        for i in range(len(num)):
            binary_ones[i] += int(num[i])
    gamma, epsilon =0,0
    binary_ones = list(map(lambda x: 1 if x > len(nums)/2 else 0, binary_ones))[::-1]
    for i in range(len(binary_ones)):
        if binary_ones[i]:
            gamma += 2**i
        else:
            epsilon += 2**i
    return gamma * epsilon


if __name__ == '__main__':

    with open('./input/day-03.ipt', 'r') as file:
        lines = [line[:-1] for line in file]
    print(binary_min_finder(lines))

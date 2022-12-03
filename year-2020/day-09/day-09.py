def xmas_fist_nonsum(nums, num_of_prev):
    prev_nums = []
    for num in nums:
        num = int(num)
        if len(prev_nums) < num_of_prev:
            prev_nums.append(num)
        else:
            sum_exists = False
            for i, prev_num in enumerate(prev_nums):
                for j in range(i, len(prev_nums)):
                    if num - prev_num == prev_nums[j] and prev_num != prev_nums[j]:
                        sum_exists = True
            if not sum_exists:
                return num
            prev_nums.append(num)
            prev_nums.pop(0)


def xmas_range(nums, weak_num):
    addends = []
    for num in nums:
        num = int(num)
        addends.append(num)
        while sum(addends) > weak_num:
            addends.pop(0)

        if sum(addends) == weak_num:
            return min(addends) + max(addends)


if __name__ == '__main__':
    with open('./input', 'r') as file:
        weak_num = xmas_fist_nonsum(file, 25)
        print(weak_num)
    with open('./input', 'r') as file:
        print(xmas_range(file, weak_num))

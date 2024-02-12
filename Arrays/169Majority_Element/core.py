def test(nums):
    counter = {}
    if len(nums) == 1:
        return nums[0]
    for element in nums:
        if element in counter:
            counter[element] += 1
        else:
            counter[element] = 1

    for key, value in counter.items():
        if value > len(nums) / 2:
            return key


print(test([8,8,7,7,7]))
def check():
    nums = [5, 1, 2, 7, 3, 4]
    S = 8
    nums = sorted(nums)
    group = []
    little_group = []
    current_sum = 0
    for i in range(0, len(nums)):
        if nums[i] > S:
            return False
    
    for num in nums:
        if current_sum + num <= S:
            little_group.append(num)
            current_sum += num
        else:
            group.append(little_group)
            little_group = [num]
            current_sum = num
    if little_group:
        group.append(little_group)
    
    return group

print(check())


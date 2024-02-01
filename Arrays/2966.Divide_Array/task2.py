def test():
    group = []
    nums = [4, 3, 2, 9, 1, 7]
    nums = sorted(nums)
    little_group = []
    D = 2
    for i in range(0, len(nums)):
        if nums[i] - nums[i-1] <= D:
            little_group.append(nums[i])
        else:
            if len(little_group) > 1: 
                group.append(little_group)
            little_group = [nums[i]]
            
    if len(little_group) > 1:
        group.append(little_group)
    
    return group

print(test())
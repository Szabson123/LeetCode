
def divideArray(nums, k):
    nums = sorted(nums)
    difference = 3
    group = []

    if len(nums) % 3 != 0:
        return group

    for i in range(0, len(nums), difference):
        if nums[i+2] - nums[i] <= k:
            group.append(nums[i:i+difference])
        else:
            return []
    return group

        
print(divideArray([17,15,20,16,15,10,20,19,17], 2))
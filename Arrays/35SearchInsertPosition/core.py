def test(nums, target):
    
    nums = sorted(nums) if target not in nums else nums
    left, right = 0, len(nums)-1  

    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return left
            

print(test([1,3,5,6], 4))
    
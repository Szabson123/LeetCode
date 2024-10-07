nums = [-4,-2,1,4,8]
close = nums[0]

for num in nums:
    if abs(num) < abs(close) or abs(num) == abs(close) and num > close:
        close = num
print(close)
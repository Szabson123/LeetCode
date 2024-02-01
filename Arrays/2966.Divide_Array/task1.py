# Masz daną tablicę liczb całkowitych nums oraz liczbę całkowitą S. Twoim zadaniem jest podzielić tablicę
# na podtablice (grupy) składające się z dowolnej liczby elementów, tak aby suma elementów w każdej podtablicy
# nie przekraczała S. Każdy element z nums musi znaleźć się w dokładnie jednej podtablicy.


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


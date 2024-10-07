# Masz daną listę liczb całkowitych nums. Twoim zadaniem jest znaleźć liczbę najbardziej oddaloną od zera w tej liście. Jeśli istnieje więcej niż jedna liczba o tej samej odległości od zera, zwróć tę, która ma większą wartość.

nums = [-4, -8, 4, 7, 8]
far = nums[0]

for num in nums:
    if abs(num) > abs(far):
        far = num
    elif abs(num) == abs(far) and num > far:
        far = num
        
print (far)
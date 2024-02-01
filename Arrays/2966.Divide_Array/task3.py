# Dana jest tablica liczb całkowitych nums. Twoim zadaniem jest podzielić tę tablicę
# na jak najmniej segmentów, gdzie każdy segment musi składać się z kolejnych elementów
# tablicy nums, które tworzą ciąg rosnący. Każdy element tablicy nums musi znaleźć się
# dokładnie w jednym segmencie.
#
# Warunki:
#
# Każdy segment musi być ciągiem rosnącym kolejnych elementów z nums.
# Każdy element nums musi być użyty dokładnie raz.
# Zwróć listę segmentów. Każdy segment to lista jego elementów.
# Jeśli istnieje wiele możliwych podziałów, zwróć dowolny z nich.

def test():
    nums = [5, 4, 2, 1, 3, 6, 7, 9, 8]
    group = []
    little_group = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            little_group.append(nums[i])
        else:
            group.append(little_group)
            little_group = [nums[i]]

    if little_group:
        group.append(little_group)
    return group


print(test())

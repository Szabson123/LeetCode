# Treść zadania:
#
# Dana jest posortowana tablica liczb całkowitych nums oraz liczba całkowita k.
# Twoim zadaniem jest podzielić tę tablicę na jak najwięcej podciągów, w których
# różnica między największą a najmniejszą liczbą w każdym podciągu jest mniejsza
# lub równa k. Każdy element tablicy nums musi znaleźć się dokładnie w jednym podciągu.
#
# Warunki:
#
# nums jest już posortowana.
# Każdy podciąg musi składać się z kolejnych elementów tablicy nums.
# Każdy element nums musi być użyty dokładnie raz.
# Zwróć listę podciągów. Każdy podciąg to lista jego elementów.
# Jeśli istnieje wiele możliwych podziałów, zwróć dowolny z nich.

def test():
    nums = [1, 2, 3, 4, 5, 5, 5, 9, 10, 11, 12]
    k = 2
    group = []
    little_group = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] - little_group[0] <= k:
            little_group.append(nums[i])
        else:
            group.append(little_group)
            little_group = [nums[i]]
    if little_group:
        group.append(little_group)

    return group


print(test())

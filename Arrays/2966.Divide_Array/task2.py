# Dana jest tablica liczb całkowitych nums oraz liczba całkowita D. Twoim zadaniem jest podzielić tę tablicę na podciągi
# (podtablice) w taki sposób, aby każdy element z nums znalazł się w dokładnie jednym podciągu, a maksymalna różnica między
# jakimikolwiek dwoma elementami w każdym podciągu była mniejsza lub równa D. Każdy podciąg powinien zawierać co najmniej dwa elementy.
# Warunki:
# Każdy element z nums musi być użyty dokładnie raz.
# Maksymalna różnica między dowolnymi dwoma elementami w podciągu nie może przekroczyć D.
# Zwróć listę podciągów jako wynik. Jeśli istnieje wiele możliwych rozwiązań, zwróć dowolne z nich. Jeśli nie można utworzyć takich podciągów, zwróć pustą listę.

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
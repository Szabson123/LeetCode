# Zadanie: Generowanie Liczb Sekwencyjnych z Określoną Sumą Cyfr
# Treść zadania:

# Napisz funkcję, która generuje wszystkie możliwe liczby sekwencyjne (w których każda kolejna cyfra jest o jeden większa niż poprzednia)
# dla zakresu cyfr od 1 do 9, ale z dodatkowym warunkiem, że suma cyfr każdej wygenerowanej liczby musi być równa określonej wartości S.
def test(S):
    empty = []
    answer = []
    
    for first_num in range(1,10):
        num = first_num 
        next_num = first_num + 1
        
        while next_num <= 9:
            num = num * 10 + next_num
            empty.append(num)
            next_num += 1
    print (empty)
            
    for num in range(0, len(empty)):
        sum_digits = sum([int(digit) for digit in str(empty[num])])
        if sum_digits == S:
            answer.append(empty[num])
            
    return answer


print(test(3))
# Opis: Masz dwie listy wyrazów list1 i list2. Połącz je w taki sposób, aby elementy naprzemiennie
#  dodawane były z obu list. Jeśli jedna lista jest dłuższa, dodaj pozostałe elementy na końcu.


list1 = ["apple", "orange", "grape"]
list2 = ["banana", "kiwi"]

i, j = 0, 0
res = []

while i < len(list1) and j < len(list2):
    res.append(list1[i])
    res.append(list2[j])

    i +=1
    j +=1

res.extend(list1[i:])
res.extend(list2[j:])

print(res)
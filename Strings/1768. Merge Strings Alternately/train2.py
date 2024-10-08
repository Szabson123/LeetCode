#Zadanie 1:
# Opis: Masz dwie sekwencje liter word1 i word2. Połącz je, dodając litery w naprzemiennym porządku,
# zaczynając od word2. Jeśli jeden ciąg jest dłuższy niż drugi, dołącz pozostałe 
# litery na koniec wynikowego ciągu.


word1 = 'abc'
word2 = 'pqrds'

i, j = 0, 0

res = []

while i < len(word1) and j < len(word2):
    res.append(word2[j])
    res.append(word1[i])

    i+=1
    j+=1

res.append(word2[j:])
res.append(word1[i:])

print(''.join(res))
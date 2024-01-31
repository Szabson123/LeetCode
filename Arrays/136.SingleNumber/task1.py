# Zadanie: Masz dany ciąg tekstowy (zdanie). Twoim zadaniem jest napisanie skryptu w Pythonie, który
# zliczy, ile razy każde słowo pojawia się w tym zdaniu i wypisze te informacje. Przyjmijmy, że słowa
# są oddzielone spacjami, a wielkość liter nie ma znaczenia (czyli 'Ala' i 'ala' to to samo słowo).


import re

zdanie = "Ala ma kota, a kot ma Alę."

# Usunięcie znaków interpunkcyjnych i zmiana na małe litery
filter_zdanie = re.sub(r'[^\w\s]', '', zdanie).lower()

# Podzielenie zdania na listę słów
lista_słów = filter_zdanie.split(" ")

print(lista_słów)

counted = {}

# Zliczanie wystąpień każdego słowa
for i in lista_słów:
    counted[i] = counted.get(i, 0) + 1

print(counted)
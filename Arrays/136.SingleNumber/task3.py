# Zadanie: Napisz skrypt w Pythonie, który zlicza, ile razy każdy znak (litera lub cyfra)
# pojawia się w danym ciągu tekstowym. Jednakże, zamiast zliczać wszystkie znaki, skrypt
# powinien zliczać tylko te znaki, które są literami (ignorując cyfry i znaki interpunkcyjne).
# Na koniec, wypisz wyniki w kolejności od najrzadziej do najczęściej występującego znaku. 
# Wielkość liter nie powinna mieć znaczenia (czyli 'A' i 'a' traktowane są jako ten sam znak).

import re

tekst = "Python 3.9 jest niesamowity! 3 razy lepszy niż 2.7."

filter_tekst = re.sub(r'[0-9.!]', '', tekst).lower()

word_list = filter_tekst.split()

podzielone_litery = [litera for slowo in word_list for litera in slowo]

counted = {}

for i in podzielone_litery:
    counted[i] = counted.get(i, 0) + 1
    
sorted_dict = dict(sorted(counted.items(), key=lambda item: item[1]))

print(sorted_dict)

# Zadanie: Napisz skrypt w Pythonie, który zlicza, ile razy każda liczba pojawia się w danej liście,
# a następnie wypisze te liczby wraz z ich liczbą wystąpień, ale tylko dla tych liczb, które pojawiają
# się więcej niż raz. Lista może zawierać zarówno liczby całkowite, jak i ułamkowe.


liczby = [3, 7.5, 3, 2, 7.5, 2, 2, 4.5, 7.5]

counted = {}

for i in liczby:
    counted[i] = counted.get(i, 0) + 1
    
for i, v in counted.items():
    if v != 1:
        print(f'{i}: {v}')
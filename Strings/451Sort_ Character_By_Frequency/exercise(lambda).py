# Ćwiczenie 1: Napisz wyrażenie lambda, które przyjmuje jeden argument (liczbę) i zwraca jego kwadrat.

# Ćwiczenie 2: Użyj wyrażenia lambda i funkcji filter(), aby wybrać z listy tylko te liczby,
# które są parzyste. Przykładowa lista: [1, 2, 3, 4, 5, 6].

# Ćwiczenie 3: Użyj wyrażenia lambda i funkcji sorted(),
# aby posortować poniższą# listę krotek po drugim elemencie każdej krotki:
# [(1, 2), (3, 1), (5, 0), (4, 2)].

# zad 1
wynik = lambda liczba: liczba*liczba
print(wynik(5))

# zad2
liczby = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, liczby))
print(even)

#zad3
counter = [(1, 2), (3, 1), (5, 0), (4, 2)]
sorting = sorted(counter, key=lambda x: x[1])

print(sorting)
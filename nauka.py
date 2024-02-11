# przywitanie = "Hello"
#
# # String
# imie = 'Szymon'
#
# # Int
# wiek = 21
#
# print(f'{przywitanie} {imie}, mam {wiek} lat')

zmienna = 4

if zmienna == 5:
    print("Masz racje!")

elif zmienna == 4:
    print("A jednak zmienna to 4")

else:
    print("Nie masz racji")




# Napisz sprawdzacz do wieku czy użytkownik moze kupic alkohol
# jesli mniej niz 18 - nie sprzedajemy
# jesli ma wiecej niz 18 ale mniej niz 25 pytamy to dowod
# jesli ma wiecej niz 25 ale mniej niz 85 to po prostu sprzedajemy
# jesli ma wiecej niz 85 to wysyłamy do domu

# wiek = 18
# if wiek < 18:
#     print("NIe sprzedajemy")
# elif wiek < 26:
#     print("Dawaj dowód")
# elif wiek < 86:
#     print("sprzedajemy")
# else:
#     print("Do domu")

# print('1')
# print('2')
# print('3')

for i in range(1, 6):
    print(i)


liczby1 = [1, 2, 3, 4, 5, 6, 7]

# print(liczby)

ogolna_lista = ['siemanko', 12, 12.5, [7, 4, 6]]

print(ogolna_lista)
print(ogolna_lista[0])

for i in ogolna_lista:
    print(i)

# for i in range(len(ogolna_lista)):
#     print(ogolna_lista[i])


liczby = [2, 2, 5, 4, 9, 6, 7]

for i in range(len(liczby)-1):
    if liczby[i] > liczby[i+1]:
        print('Lewy większy od prawego')
    else:
        print('Lewy nie jest większy od prawego')


# lista_zakupow = ['mleko', 'por', 'chleb']
#
#
# lista_zakupow.append('masło')
#
# print(lista_zakupow)
#
# lista_zakupow.pop(0)
#
# print(lista_zakupow)
#
# if 'jaja' not in lista_zakupow:
#     lista_zakupow.append('jaja')
#
# print(lista_zakupow)


lista_zakupow = ['Dubaj', 'Cypr', 'Budapeszt', 'Londyn']

lista_zakupow.append('Madera')
print(lista_zakupow)

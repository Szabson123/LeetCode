# Ćwiczenie 1: Użyj metody .join(), aby połączyć poniższą listę słów w jeden
# ciąg tekstowy, gdzie każde słowo jest oddzielone przecinkiem. Lista: ["jabłko", "banan", "pomarańcza"].

# Ćwiczenie 2: Stwórz ciąg tekstowy, w którym każda litera z poniższego
# słowa jest oddzielona znakiem gwiazdki (*). Słowo: "python".

# Ćwiczenie 3: Użyj metody .join() i wyrażenia lambda, aby połączyć liczby
# z listy w jeden ciąg tekstowy, gdzie każda liczba jest oddzielona spacją.
# Przed połączeniem konwertuj liczby na tekst. Lista: [1, 2, 3, 4, 5].

# ZAD1

lista = ["jabłko", "banan", "pomarańcza"]

new_list = ', '.join(lista)

print(new_list)

# ZAD2

word = 'python'
tekst = [tekst for tekst in word]

done = '*'.join(tekst)
print(done)
# LUB

word1 = 'python'
done1 = '*'.join(word)

print(done1)

# ZAD3

list_to_done = [1, 2, 3, 4, 5]

strings = [str(list_to_done) for list_to_done in list_to_done]

done3 = ' '.join(strings)

print(strings)
print(done3)
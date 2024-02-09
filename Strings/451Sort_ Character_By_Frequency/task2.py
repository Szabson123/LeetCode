# Zadanie: Filtrowanie i Łączenie Napisów
# Masz listę słów (napisów) oraz listę kryteriów, które określają, jakie
# słowa powinny zostać wybrane. Twoim zadaniem jest:
#
# Użyć wyrażenia lambda i funkcji filter() do wybrania słów z listy, które
# spełniają określone kryteria.
# Kryterium: Słowo musi zaczynać się na literę "p" lub zawierać literę "a".
# Po wyfiltrowaniu słów, użyj metody .join() do połączenia ich w jeden ciąg tekstowy,
# gdzie każde słowo jest oddzielone przecinkiem i spacją.
# Wydrukuj wynikowy ciąg.

words = ["python", "java", "perl", "javascript", "c#", "ruby", "pascal"]

list_filter = filter(lambda word: word[0] == 'p' or 'a' in word, words)

done = ', '.join(list_filter)

print(done)
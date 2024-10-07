word1 = 'ab'
word2 = 'pqrs'

# word1_list = [char for char in word1]
# word2_list = [char for char in word2]

# full_list = zip(word1_list, word2_list)

# full_list = list(full_list)

# list_after = []

full_list = zip(word1, word2)

list_after = []

for a, b in full_list:
    list_after.append(a)
    list_after.append(b)
    
x = ''.join(list_after)
print(x)
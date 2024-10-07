word1 = 'abc'
word2 = 'pqr'

word1_list = [char for char in word1]
word2_list = [char for char in word2]

marged_list = []

for letter in range(word1_list, word2_list):
    marged_list.append(word1_list[letter])
    marged_list.append(word2_list[letter])
    
print(marged_list)
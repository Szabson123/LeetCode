word1 = 'abc'
word2 = 'pqrds'


i, j = 0, 0
res = []

while i < len(word1) and j < len(word2):
    res.append(word1[i])
    res.append(word2[j])

    i+=1
    j+=1

res.append(word1[i:])
res.append(word2[j:])

print("".join(res))
s = 'tree'

digit = [digit for digit in s]

counter = {}

for element in digit:
    if element in counter:
        counter[element] += 1
    else:
        counter[element] = 1

sorted_chart = sorted(counter.items(), key=lambda x: x[1], reverse=True)
result = ''.join([char * freq for char, freq in sorted_chart])

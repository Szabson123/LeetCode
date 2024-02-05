

def test(s, k):
    
    filter_s = s.lower()
    counter = {}
    
    for element in filter_s:
        if element in counter:
            counter[element] += 1
        else:
            counter[element] = 1
            
    print(counter)
    
    for index, element in enumerate(filter_s):
        if counter[element] == k:
            return index
    
    return -1


print(test(s='Indivisibilities', k=7))


def test(s):

    digit = [digit for digit in s]

    counter = {}

    print(digit)

    for element in digit:
        if element in counter:
            counter[element] += 1
        else:
            counter[element] = 1
    
    for index, element in enumerate(digit):
        if counter[element] == 1:
            return index
    
    return -1    
        
        
        
print(test(s='lleetcode'))


def test(s):
    counter = {}
    digits = [digits for digits in s]
    
    for element in digits:
        if element in counter:
            counter[element] += 1
        else:
            counter[element] = 1
            
    
    for index, element in reversed(list(enumerate(digits))):
        if counter[element] == 1:
            return index
        
    return -1
        

print(test(s='testtest'))
        
        
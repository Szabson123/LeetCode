def romanToInt(s):
    data = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    total = 0
    prev_num = 0

    for char in reversed(s):
        value = data[char]
        
        if value < prev_num:
            total -= value
        else:
            total += value
        
        prev_num = value

    return total 

x = romanToInt('MCXI')

print(x)


def test(low, high):
    all = []
    for start_digit in range(1,10):
        num = start_digit
        next_digit = start_digit + 1
        
        while next_digit <= 9:
            num = num*10 + next_digit
            if num >= low and num <= high:
                all.append(num)
            next_digit += 1
    return sorted(all)

print(test(100,300))

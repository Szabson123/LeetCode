def test(low, high):
    group = []
    num1 = 0
    num2 = 1

    if high >= num1 >= low:
       group.append(num1)
    if high >= num2 >= low:
       group.append(num2)    

    
    while True:
        num2 = num1 + num2
        num1 = num2 - num1
        if num2 < low:
            continue
        if num2 <= high:
            group.append(num2)
        else:
            break
        
    return group

print(test(2,121393))
    
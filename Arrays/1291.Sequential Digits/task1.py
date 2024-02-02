empty = []
answer = []
low = 100
high = 13000


for start_digit in range(1,10):
    num = start_digit
    next_digit = start_digit + 1
    
    while next_digit <= 9:
        num = num*10+next_digit
        empty.append(num)
        next_digit += 1
        
for i in range(0, len(empty)):
    if high >= empty[i] >= low:
        answer.append(empty[i])
    
        
print (sorted(answer))
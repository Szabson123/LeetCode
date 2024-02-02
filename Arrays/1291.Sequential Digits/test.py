group = []
high = 100
low = 10
num1 = 0
num2 = 1

while True:
    num2 = num1 + num2
    num1 = num2 - num1
    if num2 < low:
        continue
    if num2 < high:
        group.append(num2)
    else:
        break
    
print(group)
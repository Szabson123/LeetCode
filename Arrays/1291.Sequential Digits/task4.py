def test(low, high):
    group = []
    for i in range(low, high):
        if len(str(i)) == len(set(str(i))):
            group.append(i)
    
    return group

print(test(100,1000000))

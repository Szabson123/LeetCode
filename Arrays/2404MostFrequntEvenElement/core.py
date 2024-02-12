def test(nums):

    counter = {}
    even_nums = list(filter(lambda x: x % 2 == 0, nums))

    if not even_nums:
        return -1
    
    for element in even_nums:
        if element in counter:
            counter[element] += 1
        else:
            counter[element] = 1
       
    majority_element = max(counter.values())
    frequent_value = [k for k, v in counter.items() if v == majority_element]
    
    return min(frequent_value)
        

print(test([8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]))

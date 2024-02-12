

def test(nums):
    counter = {}
    answer = []
    
    for element in nums:
        if element in counter:
            counter[element] +=1
        else:
            counter[element] = 1
            
    for key, element in counter.items():
        if element > len(nums)/3:
            answer.append(key)
            
    return answer


print(test([1,2]))
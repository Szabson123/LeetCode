
nums = [4,1,2,1,2]
counted= {}

for i in nums:
    counted[i] = counted.get(i, 0) + 1
for i,v in counted.items():
    if v == 1:
        print(i)

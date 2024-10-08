def maxProfit(prices):

    sum_counters = 0
    point_s = 0
    point_t = 0
    
    # for i in range(len(prices)):
    #     for j in range(i+1, len(prices)):
    #         x = prices[i] * -1 + prices[j]
    #         if x > sum_counters:
    #             sum_counters = x  
    # return sum_counters
    
    while point_s < len(prices):
        if point_t + 1 < len(prices):
            x = prices[point_s] * -1 + prices[point_t + 1]
            if x > sum_counters:
                sum_counters = x
            point_t += 1
        else:
            point_s += 1
            point_t = point_s
        
    return sum_counters
    
    
print(maxProfit([7,1,5,3,6,4]))
def solution(prices):
    l, r = 0, 1
    max_profit = 0
    
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r]-prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1
    print(max_profit)
    
solution([7,6,4,3,1])
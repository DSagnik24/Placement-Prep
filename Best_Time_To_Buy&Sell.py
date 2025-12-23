def max_profit(prices):
    l=0
    r=1
    max_profit = 0

    while(r<len(prices)):
        if prices [r]>prices[l]:
            profit = prices[r]-prices[l]
            max_profit = max(max_profit,profit)
        else:
            l=r
        r+=1

    return max_profit

prices = [7,1,5,3,6,9]
print(max_profit(prices)) 
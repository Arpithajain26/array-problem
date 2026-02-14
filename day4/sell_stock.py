def sell_stock(nums):
    mini=nums[0]
    profit=0
    """if u are selling on ith day you can buy on the
      mini price from 1st->(i-1) here 1 is the minimum"""
    for i in range(len(nums)):
        cost=nums[i]-mini
        profit=max(cost,profit)
        mini=min(mini,nums[i])
        """we used mini here,mini is updated for each itearyion,for next nums[i] we can easily find the mini"""
    return profit
print(sell_stock([7,1,5,3,6,4]))
def sell_stock1(nums):
    mini=nums[0]
    profit=0
    for i in range(len(nums)):
        cost=nums[i]-mini
        profit=max(cost,profit)
        mini=min(mini,nums[i])
    return profit
print(sell_stock1([7,1,5,3,6,4]))

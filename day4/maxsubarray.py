def maxsubarray(nums):
    maxelm=0
  
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            sum=0
            for k in range(i,j+1):
                sum+=nums[k]
            maxelm=max(maxelm,sum)
    return maxelm
print(maxsubarray([-2,-3,4,-1,-2,1,5,-3])) 
"""time complexity is o(n^3) and space complexity is o(1)"""


# better approach solution
def maxsubarray1(nums):
    maxelm=0
    for i in range(len(nums)):
        sum=0
        for j in range(i,len(nums)):
            sum+=nums[j]
            maxelm=max(maxelm,sum)
    return maxelm
print(maxsubarray1([-2,-3,4,-1,-2,1,5,-3]))

# optimal solution
"""kadane's algorithm for optimal solution 
it states that if the sum is +ve then carry forward otherwise set sum=0,this is the main logic of 
this"""
def kadane(nums):
    sum=0
    maxelm=0
    for i in range(len(nums)):
        sum+=nums[i]
        if sum<0:
            sum=0
        else:
            maxelm=max(maxelm,sum)
    return maxelm
print(kadane([-2,-3,4,-1,-2,1,5,-3]))

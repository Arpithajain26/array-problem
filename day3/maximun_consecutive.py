def maximum_consecutives(nums):
    maxelm=0
    count=0
    for i in range(len(nums)):
        if nums[i]==1:
            count+=1
            maxelm=max(maxelm,count)
        else:
            count=0
    return maxelm
print(maximum_consecutives([1,1,0,1,1,1]))





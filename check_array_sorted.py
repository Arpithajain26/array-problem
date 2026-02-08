def sortedarray(nums):
    largest=nums[0]
    for i in range(1,len(nums)):
        if nums[i-1]>nums[i]:
            return False
        
    return True

print(sortedarray([1,2,3,4,5,61,100,50]))
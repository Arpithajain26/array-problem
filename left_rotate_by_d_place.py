def leftrotate(nums,d):
    temp=[]
    for i in range(d):
        temp.append(nums[i])
        #temp=[1,2,3]
    
    for i in range(d,len(nums)):
        nums[i-d]=nums[i]
    for i in range(len(nums)-d,len(nums)):
        nums[i]=temp[i-(len(nums)-d)]
    return nums
print(leftrotate([1,2,3,4,5,6,7],3))
def movezeroes(nums):
    temp=[]
    for i in range(len(nums)):
        if nums[i]!=0:
            temp.append(nums[i])
    for i in range(len(temp)):
        nums[i]=temp[i]
    for i in range(len(temp),len(nums)):
        nums[i]=0
    return nums
        
nums=[1,0,4,0,2,0,0,1]
print(movezeroes(nums))

"""this is bruteforce approach where time complexity is o(2n) and """
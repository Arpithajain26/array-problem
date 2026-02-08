def secondlargest(nums):
    nums.sort()
    largest=nums[-1]
    secondlargest=0
    for i in range(len(nums)-2,-1,-1):
        if nums[i]!=largest:
            secondlargest=nums[i]
            break
    return secondlargest
            
print(secondlargest([1,7,7,7,7,7]))


# better solution
def secondlargest1(nums):
    largest=nums[0]
    for i in range(len(nums)):
        if largest<nums[i]:
            largest=nums[i]
    secondlargest=-1
    for i in range(len(nums)):
        if nums[i]>secondlargest and nums[i]<largest:
            secondlargest=nums[i]
    return secondlargest
print(secondlargest1([1,7,7,7,7,7]))
print(secondlargest1([1,2,4,7,7,5]))


# optimal solution
def secondlargest2(nums):
    largest=nums[0]
    secondlargest=-1
    for i in range(len(nums)):
        if nums[i]>largest:
            secondlargest=largest
            largest=nums[i]
        elif nums[i]>secondlargest and nums[i]!=largest:
            secondlargest=nums[i]
        
    return secondlargest
print(secondlargest2([1,7,7,7,7,7])) 
print(secondlargest2([1,2,4,7,7,5]))

        




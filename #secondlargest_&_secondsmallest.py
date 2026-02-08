
#optimal solution to find second largest and second smallest element in the array

def secondlargest(nums):
    largest=nums[0]
    secondlargest=-1
    for i in range(len(nums)):
        if nums[i]>largest:
            secondlargest=largest
            largest=nums[i]
        elif nums[i]>secondlargest and nums[i]!=largest:
            secondlargest=nums[i]
    return [largest,secondlargest]
def secondsmallest(nums):
    smallest=nums[0]
    secondsmallest=nums[-1]
    for num in nums:
        if num<smallest:
            secondsmallest=smallest
            smallest=num
        elif num!=smallest and num<secondsmallest:
            secondsmallest=num
    return [smallest,secondsmallest]
def secondlargest_secondsmallest(nums):
    return [secondsmallest(nums),secondlargest(nums)]
print(secondlargest_secondsmallest([2,3,1,5,6,7,8]))

    
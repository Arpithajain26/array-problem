def leftrotate(nums):
    temp=nums[0]
    for i in range(1,len(nums)):
        nums[i-1]=nums[i]
    nums.append(temp)
    return nums
print(leftrotate([1,2,3,4,5,6]))
"""the time complexity for solving this is o(n)
and space complexity for solving this is o(n)
and extra space that u have used is o(1)"""

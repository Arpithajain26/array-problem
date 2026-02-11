"""rotating array bruteforce approach may take o(n+d) time complexity but using optimal solution we can reduce it to minimum o(2n) but
space complexity is reduced to o(1)
for eg: nums=[1,2,3,4,5,6,7,8,9] first we need to right upto d here d=3 hence [1,2,3] and another is [4,5,6,7,8,9]
reverse both [3,2,1] and [9,8,7,6,5,4]  and final array for as of now [3,2,1,9,8,7,6,5,4] and now reverse full array [4,5,6,7,8,9,1,2,3]



"""
def rotatenums(nums,d):
    n=len(nums)
    nums[:d]=reversed(nums[:d])
    nums[d:]=reversed(nums[d:])
    nums[:]=reversed(nums[:])
    return nums
nums=[1,2,3,4,5,6,7,8,9]
print(rotatenums(nums,3))

        
    
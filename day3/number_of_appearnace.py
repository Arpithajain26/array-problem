def appearance(nums):
    mpp={}
    for i in range(len(nums)):
        mpp[nums[i]]=mpp.get(nums[i],0)+1
    for i,j in mpp.items():
        if j==1:
            return i
    return
print(appearance([1,1,2,3,3,4,4]))

def appearance1(nums):
    xor=0
    for num in nums:
        xor^=num
    return xor
print(appearance1([1,1,2,3,3,4,4]))
        


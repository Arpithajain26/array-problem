def majorityelement(nums,n):
    mpp={}
    for i in range(len(nums)):
        mpp[nums[i]]=mpp.get(nums[i],0)+1
    for key,value in mpp.items():
        if value>(n//2):
            return key
    return 
print(majorityelement([2,2,3,3,1,2,2],7))
# optimize solution by using hashmap

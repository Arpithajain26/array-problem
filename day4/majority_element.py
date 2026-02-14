def majorityelement(nums,n):
    for i in range(len(nums)):
        count=0
        for j in range(len(nums)):
            if nums[i]==nums[j]:
                count+=1
        if count>(n//2):
            return nums[i]
    return
print(majorityelement([2,2,3,3,1,2,2],7))
"""majority element ,this is the bruteforce approach"""
                           


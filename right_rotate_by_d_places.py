"""right rotate by d places nums=[1,2,3,4,5,6,7] d=3 the answer should be [5,6,7,1,2,3,4] optimal solution for this is that
first we need to divide [1,2,3,4] and [5,6,7] reverse both small arrays [4,3,2,1] and [7,6,5] ,now full array is=[4,3,2,1,7,6,5] 
and now reverse full array [5,6,7,1,2,3,4]
"""
def rotateright(nums,d):
    nums[d:]=reversed(nums[d:])
    nums[:d]=reversed(nums[:d])
    nums[:]=reversed(nums[:])
    return nums
nums=[1,2,3,4,5,6,7]
print(rotateright(nums,3))
"""bruteforce approach
nums=[1,2,3,4,5,6,7] temp=[5,6,7]"""
def rightrotate(nums,d):
    temp=[]
    n=len(nums)
    for i in range(n-d,n):
        temp.append(nums[i])
        #temp=[5,6,7]
    for i in range(len(nums)-1,d-1,-1):
        nums[i]=nums[i-d]
    
    for i in range(d):
        nums[i] = temp[i]
    return nums
print(rightrotate([1,2,3,4,5,6,7],3))
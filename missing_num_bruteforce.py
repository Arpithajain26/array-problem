def missing_number(nums):

    for i in range(1,len(nums)+1):
        flag=0
        for j in range(0,len(nums)-1):
            if nums[j]==i:
                flag=1
                break
        if flag==0:
            return i
    return 
print(missing_number([1,2,4,5]))
"""time complexity is o(n*n) and the space complexity is o(1)"""



"""better solution"""
def missing_number1(nums):
    n=len(nums)
    hash=[0]*(n+1)
    for i in range(0,n-1):
        hash[nums[i]]=1
    for i in range(1,n+1):
        if hash[i]==0:
            return i
    return
print(missing_number1([1,2,4,5]))
"""time complexity is o(2n) and space complexity is o(n)"""


'''optimal solution'''
def missing_number2(nums,N):
    n=len(nums)
    sum1=sum(nums)
    sum2=(N*(N+1))//2
    return sum2-sum1
print(missing_number2([1,2,4,6,7,5],7))


        

def missing_number(nums,n):
    xor1=0
    for i in range(1,n+1):
        xor1=xor1^i
    xor2=0
    for i in range(len(nums)):
        xor2=xor2^nums[i]
    return xor1^xor2
print(missing_number([1,2,3,5],5))
# another approach as this takes o(2n)
def missing_number1(nums,n):
    xor1=0
    xor2=0
    for i in range(len(nums)):
        xor2=xor2^nums[i]
        xor1=xor1^(i+1)
    xor1=xor1^n
    return xor1^xor2
print(missing_number1([1,2,3,5],5))
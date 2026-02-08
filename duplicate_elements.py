def duplicatenums(nums):
    duplicate=len(list(set(nums)))
    return duplicate
print(duplicatenums([3,4,3,4,3,2]))
# another method
def duplicatenums2(nums):
    duplicate=set()
    for num in nums:
        duplicate.add(num)
    return len(duplicate)
print(duplicatenums2([3,4,3,4,3,2]))
# optimal solution
def duplicatenums3(nums):
    i=0
    for j in range(1,len(nums)):
        if nums[i]!=nums[j]:
            i+=1
            nums[i]=nums[j]
    return i+1
print(duplicatenums3([3,3,4,5,6]))
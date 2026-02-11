def linear_search(nums,key):
    for i in range(len(nums)):
        if nums[i]==key:
            return i
    return -1
print(linear_search([1,2,3,4,23,43],4))

print(linear_search([1,2,3,4,23,43],46))


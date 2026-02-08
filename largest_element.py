"""Given an array of integers nums, return the value of the largest element in the array


Example 1

Input: nums = [3, 3, 6, 1]

Output: 6

Explanation: The largest element in array is 6

Example 2

Input: nums = [3, 3, 0, 99, -40]

Output: 99

Explanation: The largest element in array is 99"""


def largest(nums):
    return max(nums)
print(largest([3,2,1,4,6]))

# another solution
def largest2(nums):
    nums.sort()
    return nums[-1]
print(largest2([2,3,4,1,6,89]))



# optimal solution
def largest3(nums):
    largestnum=nums[0]
    for i in range(len(nums)):
        if nums[i]>largestnum:
            largestnum=nums[i]
    return largestnum
print(largest3([2,3,4,1,3,5]))
def movezeros(nums):
    j=-1
    for i in range(len(nums)):
        if nums[i]==0:
            j=i
            break
    for i in range(j+1,len(nums)):
        if nums[i]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            j+=1
    return nums
print(movezeros([1,0,3,2,0,0,4,5,6]))
'''what means first we need to start with the array if nums[i] is 0 
then we need set that as j to track later then again we need to run 
2nd for loop for that we need to check if num[i]!=0 if so then swaping
 takes plcae btn nums[i] and nums[j] and then returning nums'''
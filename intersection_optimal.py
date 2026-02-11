def intersection_of_2_arrays(num1,num2):
    a,b=len(num1),len(num2)
    i,j=0,0
    intersection=[]
    while i<a and j<b:
        if(num1[i]<num2[j]):
            i+=1
        elif(num2[j]<num1[i]):
            j+=1
        else:
            intersection.append(num1[i])
            i+=1
            j+=1


    return intersection
print(intersection_of_2_arrays([1,2,3,4,5],[2,3,4,5,6,7]))
"""time complexity o(n1+n2) space complexity is o(1)"""




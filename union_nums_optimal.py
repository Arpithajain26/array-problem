def union_nums(num1, num2):
    i = j = 0
    n, m = len(num1), len(num2)
    union = []

    while i < n and j < m:
        if num1[i] <= num2[j]:
            if not union or union[-1] != num1[i]:
                union.append(num1[i])
            i += 1
        else:
            if not union or union[-1] != num2[j]:
                union.append(num2[j])
            j += 1

    while i < n:
        if not union or union[-1] != num1[i]:
            union.append(num1[i])
        i += 1

    while j < m:
        if not union or union[-1] != num2[j]:
            union.append(num2[j])
        j += 1

    return union
print(union_nums([1,2,3,4,5,6],[2,3,4,5,6,7,8,9]))
"""time complexity is o(n1+n2) and space complexity is 0(n1+n2)"""

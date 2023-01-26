def maximumSum(a, m):
    a = list(map(lambda x:x%m,itertools.accumulate(a)))
    maxi = max(a)
    arr = []
    for i in a:
        bisect.insort(arr,i) #the bisect module in Python assists in preserving a list in a sorted order, as it bypasses the sort operation after each insertion
        if i!=arr[-1]:
            maxi = max(maxi,(i-arr[bisect.bisect_right(arr,i)])%m)
    return maxi



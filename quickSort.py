def quicksort(sequence):
    length=len(sequence)
    if(length<=1):
        return sequence
    else:
        pivot=sequence.pop()

    greater=[]
    lower=[]
    for i in sequence:
        if i<pivot:
            lower.append(i)
        else:
            greater.append(i)

    return quicksort(lower) + [pivot] + quicksort(greater)




print(quicksort([4,2,3,6,8,4,10,0,77]))

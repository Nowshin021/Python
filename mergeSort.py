print("Merge sort || Devide and concure ")
##find midpoint -> devide the array -> sort devided array -> merge those sorted array
def merge(a,list_1,list_2):
    i = 0
    j = 0
    k = 0
    while (i < len(list_1) and j < len(list_2)):
        if (list_1[i] <= list_2[j]):
            a[k] = list_1[i]
            i = i + 1
        else:
            a[k] = list_2[j]
            j = j + 1
        k = k + 1

    while (i < len(list_1)):
        a[k] = list_1[i]
        i = i + 1
        k = k + 1

    while (j < len(list_2)):
        a[k] = list_2[j]

        j = j + 1
        k = k + 1


def mergesort(a):
    #recursive base case
    if(len(a)>1):
        mid=len(a)//2
        #devide into 2 sub list

        list_1=[]
        list_2=[]
        for i in range(mid):
            list_1.append(a[i])
        for j in range(mid,len(a)):
            list_2.append(a[j])

        #recurse
        mergesort(list_1)
        mergesort(list_2)
        merge(a,list_1,list_2)



print("Enter how many numbers ? ")
n=int(input())
arr=[]
for i in range(n):
    p=int(input())
    arr.append(p)


mergesort(arr)
print("Sorted list " , arr)





def Selection(a,l):
    for i in range(0,l):
        min=i
        for j in range(i+1,l):
            if(a[min]>a[j]):
                min=j
        a[i],a[min]=a[min],a[i]



print("Enter how many numbers ? ")
n=int(input())
arr=[]
for i in range (0,n):
    p=int(input())
    arr.append(p)
print()
print("Original data : ",arr )
Selection(arr,len(arr))
print("Sorted array")

print(arr)

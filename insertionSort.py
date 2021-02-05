print("Insertion Sort")
j=int()
def InsertionSort(a,n):
    for i in range(n):
        temp=a[i]
        j=i-1
        while(j>=0 and a[j]>temp):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=temp




print("How many numbers ? ")
n=int(input())
print("Enter numbers : ")
arr=[]
for i in range(n):
    p=int(input())
    arr.append(p)


print("Original data : " , arr)
InsertionSort(arr,n)
print("Sorted : " , arr)

print()
def bubbleRecursive(a,n):
    if n==1:
        return
    for j in range(0,n-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    bubbleRecursive(a,n-1)

print("Enter how many numbers ? ")
n=int(input())
arr=[]
for i in range (0,n):
    p=int(input())
    arr.append(p)
print()



bubbleRecursive(arr,n)
print(arr)

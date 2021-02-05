#bubble sort
print()
print("Enter how many numbers ? ")
n=int(input())
arr=[]

def bubbleA(a1):
    n = len(a1)
    for i in range(n - 1):
        for j in range(0, n  - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubbleB(a2):
    n = len(a2)
    for i in range(n - 1):
        for j in range(0, n  - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

for i in range (0,n):
    p=int(input())
    arr.append(p)
print()
print("Original data : " )
print(arr)
print()
bubbleA(arr)
print("assending sort ",arr)
bubbleB(arr)
print("Decending sort ",arr)





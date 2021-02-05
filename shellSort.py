print("Shell sort : ")


def shellSort(arr):
    n=len(arr)
    gap=n//2
    while gap>0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j =j- gap

            arr[j] = temp
        gap =gap// 2



a=[12,25,86,41,1,7,30,25,9]
shellSort(a)
print(a)

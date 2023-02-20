def sorting_algorithm(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[23,1,4,38,3]
input_1=sorting_algorithm(arr)
print(arr)



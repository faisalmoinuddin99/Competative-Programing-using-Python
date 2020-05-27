def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

arr = [7,3,1,5,2]
max_score = bubble(arr)
for i in range(len(max_score)):
    if arr[0] < arr[i]:
        arr[0] = arr[i]
print(f"Highest timing record: {arr[0]}")
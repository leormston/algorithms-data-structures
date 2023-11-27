
def bubbleSort(arr):
    print(f"Bubble Sorting {arr}")
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)- 1- i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)


if __name__ == "__main__":
    arr = [1 ,2, 5, 2, 3, 6, 7, 6]
    bubbleSort(arr)

    arr = [1 ,2, 6, 7, 6, 5, 2, 3]
    bubbleSort(arr)

    arr = [1 ,2, 6, 7, 6, 5, 2, 3, 7, 6, 5, 2, 3, 7, 6, 5, 2, 3]
    bubbleSort(arr)
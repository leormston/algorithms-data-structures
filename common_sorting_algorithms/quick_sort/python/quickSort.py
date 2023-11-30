
def quick_sort(arr, lo, hi):
    #base cases
    print(arr)
    if (lo < hi):    
        pivot_index = partition(arr, lo, hi)
        
        quick_sort(arr, lo, pivot_index-1)
        quick_sort(arr, pivot_index + 1, hi)
        


def partition(arr, lo, hi):
    pivot = arr[hi]

    index = lo - 1

    #put everything that is less than chosen pivot (we chose last element in the array) at the start of the array
    for i in range(lo, hi, 1):
        if(arr[i] <= pivot):
            index += 1;
            tmp = arr[i]
            arr[i] = arr[index]
            arr[index] = tmp 

    #this step here is to move the pivot value past the last inserted item
    index += 1
    arr[hi] = arr[index]
    arr[index] = pivot

    #this is then returning the pivot index
    return index


if __name__ == "__main__":
    arr = [9, 3, 7 , 4, 69, 420, 42]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)
#Binary search finds the index of a value in an array
#This algorithm only works in a sorted array
#returns -1 if the key does not exist in the array

def binarySearch(key, arr):
    print(f'Binary Searching for {key} in array')
    try:
        print(f'Answer should be:  {arr.index(key)}')
    except Exception as e:
        print('Answer should be: Key is not in array')

    lo = 0
    hi = len(arr)
    while(lo < hi):
        mid =  int(lo + (hi - lo) / 2)
        print(f'hi: {hi}, mid: {mid}, lo: {lo}')
        if key < arr[mid]:
            hi = mid 
        elif key > arr[mid]:
            lo = mid + 1
        elif key == arr[mid]:
            return mid
    return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 8, 12, 234, 234235, 234342354, 23423546546745, 2342423456434574]
    print(binarySearch(7, arr))
    print(binarySearch(1, arr))
    print(binarySearch(2, arr))
    print(binarySearch(234, arr))
    print(binarySearch(23423546546745, arr))
    print(binarySearch(2342423456434574, arr))
def linearSearch(key, arr):
    #This is a linear search algorithm determining if the given value exists
    # It does not return the index althought the big O notation complexity value would be the same
    for i in range(len(arr)):
        if arr[i] == key:
            return True
    return False


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 8, 12, 234, 234235, 234342354, 23423546546745, 2342423456434574]

    print(linearSearch(7, arr)) #False
    print(linearSearch(1, arr)) #True
    print(linearSearch(2, arr)) #True
    print(linearSearch(234, arr)) #True
    print(linearSearch(2342354654674522, arr)) #False
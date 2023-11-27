import math

def twoCrystalBalls(arr):
    jumping = math.floor(math.sqrt(len(arr)))
    index = 0

    while(index < len(arr) and arr[index] == 0):
        index += jumping

    index = index - jumping
    if index < 0:
        index = 0
    
    count = 0

    while(index < len(arr)):
        print(count)
        count += 1
        if arr[index] == 1:
            return index 
        index += 1
        


if __name__ == "__main__":
    print("starting")
    arr = [0, 0, 0, 0, 0, 1] #5
    arr_two = [0, 1, 1, 1, 1, 1, 1] #1
    arr_three = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1] #10
    print(f"Highest Height Ball will not break at {twoCrystalBalls(arr)}")
    print(f"Highest Height Ball will not break at {twoCrystalBalls(arr_two)}")
    print(f"Highest Height Ball will not break at {twoCrystalBalls(arr_three)}")

    
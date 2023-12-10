import math
class MinHeap():
    """smallest values at the top of tree and it goes down in descending order"""

    def __init__(self, length=0, data=[]):
        self.length = length
        self.data = data

    def insert(self, val):
        """inserting into the minHeap"""
        self.data.append(val)
        self.heapifyUp(self.length)
        self.length += 1

    def delete(self):
        """delete is sometimes also known as pop or poll in heaps"""
        """we delete first element of array and overwrite it with the last element of the array"""
        """Then we heapify down"""
        if (self.length == 0):
            return
    
        return_val = self.data[0]
        self.length -= 1
        
        if(self.length == 0):
            self.data = []
            self.length = 0
            return return_val
        
        self.data[0] = self.data[self.length]
        self.heapifyDown(0)
        return return_val

    def heapifyDown(self, index):
        """checking if which child is smallest and whether it should be swapped with current (child parent)"""        
        leftIndex = self.leftChild(index)
        rightIndex = self.rightChild(index)

        if(index >= self.length or leftIndex >= self.length):
            return

        leftVal = self.data[leftIndex]
        rightVal = self.data[rightIndex]
        currentVal = self.data[index]

        if (leftVal > rightVal and currentVal > rightVal):
            #if right val is the smallest and yet still current val is bigger than right
            self.data[rightIndex] = currentVal
            self.data[index] = rightVal
            self.heapifyDown(rightIndex)

        elif(rightVal > leftVal and currentVal > leftVal):
            #if left val is the smallest and yet still current val is smaller than left
            self.data[leftIndex] = currentVal
            self.data[index] = leftVal
            self.heapifyDown(leftIndex)

    def heapifyUp(self, index):
        """checking if parent is larger then current and swapping if so recursively"""
        if(index == 0):
            return
        parent = self.data[self.parent(index)]
        value = self.data[index]

        if parent > value:
            #if parent is greater than value
            #go up and swap value of current and parent
            self.data[index] = parent
            self.data[self.parent(index)] = value
            self.heapifyUp(parent)


    def parent(self, index):
        """returns parent index of a given passed index"""
        return math.floor((index-1) / 2)
    
    def leftChild(self, index):
        return (index * 2) + 1
    
    def rightChild(self, index):
        return (index * 2) + 2

if __name__ == "__main__":
    min_heap = MinHeap()
    print(min_heap.parent(6)) #should be 2
    print(min_heap.parent(4)) #should be 1
    min_heap.insert(1)
    min_heap.insert(3)
    min_heap.insert(4)
    min_heap.insert(2)
    min_heap.insert(5)
    min_heap.insert(10)

    print(min_heap.delete()) #should be 1
    print(min_heap.delete()) #should be 2
    print(min_heap.delete()) #should be 3
    min_heap.insert(24)
    print(min_heap.delete()) #should be 





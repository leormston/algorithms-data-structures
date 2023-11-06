class BinarySearch
{
    public static int binarySearch(int key, int[] arr)
    {
        int lo = 0;
        int hi = arr.length;
        int mid;
        while(lo <= hi)
        {
            mid = (int) ((lo + hi) / 2);
            if (arr[mid] == key) return mid;
            else if (arr[mid] > key) hi = mid- 1;
            else if (arr[mid] < key) lo = mid + 1;
        }
        return -1;
    }
    
    public static void main(String[] args)
    {
        int[] vals = {1, 2, 3, 4, 5, 6, 8, 12, 234, 234235, 2342354, 23465465, 234242345};
        
        //Some simple tests just to prove that it works...
        System.out.println(binarySearch(4, vals));
        System.out.println(binarySearch(6, vals));
        System.out.println(binarySearch(8, vals));
        System.out.println(binarySearch(234, vals));
        System.out.println(binarySearch(23465465, vals));

    }
}
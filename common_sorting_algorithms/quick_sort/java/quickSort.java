class QuickSort
{

    public static void printArr(int[] arr)
    {
        String string_arr = "";
        for(int i = 0; i < arr.length; i++)
        {
            string_arr += arr[i] + ", ";
        }
        System.out.println(string_arr);
    }
    public static void quicksort(int[] arr, int lo, int hi)
    {
        //base case is whenever lo is not less than hi. So this is the step case
        printArr(arr);
        if(lo < hi)
        {
            //run partition once and find a pivot
            int pivot = partition(arr, lo, hi);

            //run quicksort on the lower half of the array (not including the pivot)
            quicksort(arr, lo, pivot-1);

            //run quicksort on the upper half of the array (not including the pivot)
            quicksort(arr,pivot+1, hi);
        }
    }

    public static int partition(int[] arr, int lo, int hi)
    {
        //set the pivot as hi
        int pivot = arr[hi];
        
        //set index one less than starting point
        int index = lo -1;

        //everything less than pivot goes ot the start of the array
        //index goes up each insert 
        for(int i = lo; i < hi; i++)
        {
            if(arr[i] < pivot)
            {
                index +=1;
                int tmp = arr[index];
                arr[index] = arr[i];
                arr[i] = tmp;
            }
        }

        //then we move the pivot to just after the last value inserted
        index += 1;
        arr[hi] = arr[index];
        arr[index] = pivot;

        //then we return index (the position of the pivot)
        return index;
    }

    public static void main(String[] args) {
        int[] arr = {420, 9, 1, 2, 3, 7, 4};
        quicksort(arr, 0, arr.length-1);
    }
}
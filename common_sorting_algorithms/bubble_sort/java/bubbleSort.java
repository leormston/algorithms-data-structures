class bubbleSort {
    public static void printArray(int[] arr)
    {   
        System.out.println("Printing Array:");
        for(int i = 0; i < arr.length; i++)
        {
            System.out.println(arr[i]);
        }
    }

    public static void bSort(int[] arr)
    {
        printArray(arr);

        for(int i = 0; i < arr.length - 1; i++)
        {
            for(int j = 0; j < arr.length - 1 - i; j++)
            {
                int tmp = arr[j];
                if(arr[j] > arr[j+1])
                {
                    arr[j] = arr[j+1];
                    arr[j+1] = tmp;
                }
            }
        }
        printArray(arr);
    }
    public static void main(String[] args)
    {
        int[] arr = {1 ,2, 5, 2, 3, 6, 7, 6};
        bSort(arr);

        int[] arr_two = {1 ,2, 6, 7, 6, 5, 2, 3};
        bSort(arr_two);
        
        int[] arr_three = {1 ,2, 6, 7, 6, 5, 2, 3, 7, 6, 5, 2, 3, 7, 6, 5, 2, 3};
        bSort(arr_three);
    }
}

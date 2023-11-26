class LinearSearch
{
    public static Boolean linearSearch(int key, int[] arr)
    {
        for(int i = 0; i < arr.length; i++)
        {
            if(arr[i] == key)
            {
                return true;
            }
        }
        return false;
    }


    public static void main(String[] args)
    {
        int[] arr = {1, 2, 3, 4, 5, 6, 8, 12, 234, 234235, 2342354, 23465465, 234242345};

        // These should return True
        System.out.println(linearSearch(4, arr));
        System.out.println(linearSearch(6, arr));
        System.out.println(linearSearch(8, arr));
        System.out.println(linearSearch(234, arr));
        System.out.println(linearSearch(23465465, arr));

        // These should return False
        System.out.println(linearSearch(0, arr));
        System.out.println(linearSearch(7, arr));
        System.out.println(linearSearch(22, arr));
    }
}
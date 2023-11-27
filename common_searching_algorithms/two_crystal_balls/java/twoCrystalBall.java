import java.lang.Math;


class twoCrystalBall {
    public static int twoCrystalBall(int[] arr){
        int jump = (int) Math.floor(  Math.sqrt(arr.length));
        int last_jump = jump;
        for(int i =jump; i < arr.length; i+= jump)
        {
            last_jump = i;
            if(arr[i] == 1)
            {
                break;
            }
        }
        int breaking_point = -1;
        for(int i = last_jump - jump; i < arr.length; i ++)
        {
            if(arr[i] == 1)
            {
                breaking_point = i;
                break;
            }
        }
        return breaking_point;
    }

    public static void main(String[] args){
        int[] arr = {0, 1, 1, 1, 1};
        int[] arr_two = {0, 0, 0, 1, 1, 1, 1, 1};
        int[] arr_three = {0, 0, 0, 0, 0, 0, 0, 1};
        int[] arr_four = {0, 0, 1};

        System.out.println(twoCrystalBall(arr));
        System.out.println(twoCrystalBall(arr_two));
        System.out.println(twoCrystalBall(arr_three));
        System.out.println(twoCrystalBall(arr_four));

        
    
    }
}

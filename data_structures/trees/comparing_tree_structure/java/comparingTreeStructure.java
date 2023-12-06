class comparingTreeStructure
{
    public static boolean compare(Node a, Node b)
    {
        if(a == null && b == null)
        {
            return true;
        }
        else if(a == null || b == null)
        {
            return false;
        }
        else if(a.val != b.val)
        {
            return false;
        }

        return compare(a.left, b.left) && compare(a.right, b.right);

    }

    public static void main(String[] args) {
        //Comparing one tree to another ensuring structure and contents are identical

        Node th_one = new Node(4);
        th_one.left = new Node(2);
        th_one.right = new Node(5);

        Node th_two = new Node(4);
        th_two.left = new Node(2);
        th_two.right = new Node(5);

        Node th_three = new Node(4);
        th_three.left = new Node(2);
        th_three.left.right = new Node(5);

        System.out.println(compare(th_one, th_two));

        System.out.println(compare(th_one, th_three));
    }
}
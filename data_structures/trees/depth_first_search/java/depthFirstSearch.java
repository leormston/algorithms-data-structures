class depthFirstSearch
{
    public static boolean search(Node curr, int val)
    {
        if(curr == null)
        {
            return false;
        }
        if(curr.val == val)
        {
            return true;
        }
        if(val > curr.val)
        {
            return search(curr.right, val);
        }
        return search(curr.left, val);
    }
    public static void main(String[] args) {
        Node bt_head = new Node(25);
        Node left = new Node(23);
        left.left = new Node(5);
        Node right = new Node(27);
        bt_head.left = left;
        bt_head.right = right;
        right.left = new Node(26);
        right.right = new Node(30);
        right.right.right = new Node(100);

        System.out.println(search(bt_head, 5)); //true

        System.out.println(search(bt_head, 23)); //true

        System.out.println(search(bt_head, 30)); //true

        System.out.println(search(bt_head, 0)); //false

        System.out.println(search(bt_head, 28)); //false

        System.out.println(search(bt_head, 2356)); //false
    }
}
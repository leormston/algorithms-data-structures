import java.util.ArrayList; 

public class postOrderTraversal {

    public static ArrayList<Integer> walk(Node curr, ArrayList<Integer> path)
    {
        if(curr == null)
        {
            return path;
        }
        
        walk(curr.left, path);
        walk(curr.right, path);
        path.add(curr.val);

        return path;
    }

    public static void main(String[] args) {
        Node head = new Node(4);
        Node left = new Node(2);
        Node right = new Node(5);
        head.left = left;
        head.right = right;

        left.left = new Node(2);
        left.left.left = new Node(0);
        left.right = new Node(3);

        right.left = new Node(10);
        right.right = new Node(20);

        ArrayList<Integer> path = new ArrayList<Integer>();

        System.out.println(walk(head, path));
    }    
}

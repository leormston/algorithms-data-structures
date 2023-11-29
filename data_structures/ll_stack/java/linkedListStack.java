import java.util.LinkedList;

class LinkedListStack
{
    Node head;
    int length = 0;

    public void peek()
    {
        if(this.length == 0)
        {
            System.out.println("Stack is empty");
        }
        else
        {
            System.out.println(this.head.val);
        }
    }

    public void pop()
    {
        if(this.length == 0)
        {
            System.out.println("Stack is empty");
        }
        else if(this.length == 1)
        {
            this.length--;
            this.head = null;
        }
        else {
            System.out.println(this.head.val);
            this.head = this.head.prev;
        }
    }

    public void push(int val)
    {
        length++;
        Node new_node = new Node(val);

        if(this.length == 1)
        {
            this.head = new_node;
        }
        else
        {
            new_node.prev = this.head;
            this.head = new_node;
        }
    }

    public static void main(String[] args)
    {
        LinkedListStack stack = new LinkedListStack();
        stack.peek();
        stack.push(1);
        stack.peek();
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.peek();
        stack.pop();
        stack.pop();
        stack.peek();

    }
}
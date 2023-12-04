import java.util.LinkedList;

class LinkedListQueue {
    Node head;
    Node tail;
    int length = 0;

    public void queue(int val)
    {
        this.length++;
        Node new_node = new Node(val);
        if(head == null)
        {
            this.head = new_node;
            this.tail = new_node;
        }
        else
        {
            this.tail.next = new_node;
            this.tail = new_node;
        }
    }

    public void dequeue()
    {
        if(this.length == 0)
        {
            System.out.println("The queue is empty");
        }
        else if (this.length == 1)
        {
            System.out.println(this.head.val);
            this.head = null;
            this.tail = null;
            this.length--;
        }
        else
        {
            System.out.println(this.head.val);
            this.head = this.head.next;
        }
    }

    public void peek()
    {
        if( this.head == null)
        {
            System.out.println("Queue is empty");
        }
        else
        {
            System.out.println(this.head.val);
        }
    }

    public static void main(String[] args)
    {
        LinkedListQueue linked_list = new LinkedListQueue();
        linked_list.queue(5);
        linked_list.peek(); //five has entered the queue and should be at front
        linked_list.queue(4);
        linked_list.queue(3);
        linked_list.queue(2);
        linked_list.queue(1);
        linked_list.peek(); //five should still be at the front
        linked_list.dequeue();
        linked_list.dequeue();
        linked_list.peek(); //three should be at the front of the queue
        linked_list.dequeue();
        linked_list.dequeue();
        linked_list.peek(); //one should be at the front of the queue
        linked_list.dequeue();
        linked_list.peek(); //queue should be at the front of the queue

    }
}

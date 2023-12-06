class DoublyLinkedList {
    Node head;
    Node tail;
    int length = 0;

    public  int getLength()
    {
        return this.length;
    }

    public  void insertAt(int index, int val)
    {
        if(index < 0 || index > this.length)
        {
            System.out.println("Index is out of bounds!");
        }
        else
        {
            if(index == 0)
            {
                prepend(val);
            }
            else if(index == this.length)
            {
                append(val);
            }
            else
            {
                Node curr = this.head;
                for(int i = 0; i < index-1; i++)
                {
                    curr = curr.next;
                }
                Node new_node = new Node(val);
                Node prev = curr.prev;
                prev.next = new_node;
                curr.prev = new_node;
                new_node.prev = prev;
                new_node.next = curr;
                this.length++;
            }
        }

    }

    public  int remove(int val)
    {
        Node curr = this.head;
        Boolean found = false;
        for(int i = 0; i < this.length; i++)
        {
            if(curr.val == val || found == true)
            {
                found = true;
            }
            else
            {
                curr = curr.next;
            }
        }

        if(found == true)
        {
            this.length--;
            if(this.length == 0){
                this.head = null;
                this.tail = null;
            }
            else
            {
                if(curr.prev != null)
                {
                    curr.prev.next = curr.next;
                }
                if(curr.next != null)
                {
                    curr.next.prev = curr.prev;
                }
            }
            return curr.val;
        }
        else
        {
            System.out.println("No node with val found");
            return -1;
        }
    }

    public  int removeAt(int index)
    {
        if (index > this.length)
        {
            System.out.println("Index is out of range");
        }
        else
        {
            Node curr = this.head;
            for(int i= 0; i < index; i++)
            {
                curr=curr.next;
            }
            this.length -=1;
            if(this.length == 0)
            {
                this.head = null;
                this.tail = null;
            }
            else 
            {
                if(curr.prev != null)
                {
                    curr.prev.next = curr.next;
                }
                if(curr.next != null)
                {
                    curr.next.prev = curr.prev;
                }
            }
            return curr.val;
        }
        return -1;
    }

    public  void append(int val)
    {
        Node new_node = new Node(val);
        if(this.length == 0)
        {
            this.head = new_node;
            this.tail = new_node;
        }
        else 
        {
            this.tail.next = new_node;
            new_node.prev = this.tail;
            this.tail = new_node;
        }
        this.length++;
    }

    public  void prepend(int val)
    {
        Node new_node = new Node(val);
        if(this.length == 0)
        {
            this.tail = new_node;
            this.head = new_node;
        }
        else
        {
            this.head.prev = new_node;
            new_node.next = this.head;
            this.head = new_node;
        }
        this.length++;
    }

    public  int get(int index)
    {
        if(index > this.length)
        {
            System.out.println("index is out of bounds");
            return -1;
        }
        else
        {
            Node curr = this.head;
            for(int i = 0; i < index; i++)
            {
                curr = curr.next;
            }
            return curr.val;
        }
    }

    public static void main(String[] args)
    {
        DoublyLinkedList dll = new DoublyLinkedList();
        dll.append(1);
        dll.append(2);
        dll.append(3);
        dll.append(4);
        dll.append(5);
        // dll.remove(4);
        System.out.println(dll.get(3));
    }

}
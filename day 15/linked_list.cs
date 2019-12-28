using System;
class Node
{
	public int data;
	public Node next;
    public Node(int d){
        data=d;
        next=null;
    }
		
}
class Solution {

	public static Node insert(Node head,int data)
	{
        Node temp = new Node(data);
        if (head == null) { // empty list becomes the new node
            head = temp;
        } else { // find last and link the new node
            Node last = head;
            while(last.next != null) 
                last=last.next;
            last.next = temp;
        }
        return head;
    }

	public static void display(Node head)
	{
		Node start=head;
		while(start!=null)
		{
			Console.Write(start.data+" ");
			start=start.next;
		}
	}
    static void Main(String[] args) {
	
		Node head=null;
        int T=Int32.Parse(Console.ReadLine());
        while(T-->0){
            int data=Int32.Parse(Console.ReadLine());
            head=insert(head,data);
        }
		display(head);
	}
}

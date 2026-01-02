import java.util.*;

class CircularLinkedList {

    static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
        }
    }

    Node last = null;


    void insert(int data) {
        Node temp = new Node(data);

        if (last == null) {
            last = temp;
            last.next = last;
            return;
        }

        temp.next = last.next;
        last.next = temp;
        last = temp;
    }


    void delete(int key) {
        if (last == null) return;

        Node curr = last.next, prev = last;

    
        if (curr == last && curr.data == key) {
            last = null;
            return;
        }

        
        do {
            if (curr.data == key) break;
            prev = curr;
            curr = curr.next;
        } while (curr != last.next);

    
        if (curr.data != key) return;

        prev.next = curr.next;

        
        if (curr == last) last = prev;
    }

    
    void display() {
        if (last == null) return;

        Node temp = last.next;
        do {
            System.out.print(temp.data + " ");
            temp = temp.next;
        } while (temp != last.next);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        CircularLinkedList list = new CircularLinkedList();

        for (int i = 0; i < n; i++) {
            list.insert(sc.nextInt());
        }

        
        list.display();
    }
}

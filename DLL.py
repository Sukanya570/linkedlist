class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Delete first occurrence of key
    def delete(self, key):
        if self.head is None:
            return

        temp = self.head

        # Case 1: head node is the one to delete
        if temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        # Search for node to delete
        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            return  # key not found

        # Remove node
        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

    # Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


# Main Program
n = int(input())                     # Number of elements
values = list(map(int, input().split()))

dll = DoublyLinkedList()

for v in values:
    dll.insert(v)

# As per sample format: only display after insertion
dll.display()

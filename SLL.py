class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    
    def delete(self, key):
        temp = self.head

        
        if temp and temp.data == key:
            self.head = temp.next
            return

        
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return  

        prev.next = temp.next

    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next



n = int(input())                     
values = list(map(int, input().split()))

ll = LinkedList()

for v in values:
    ll.insert(v)


ll.display()

# constructor: node and LL
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, node):
        self.head = node
        self.tail = node
        self.length = 1
    
    # __str__ (I decided to define this method for convenience)
    def __str__(self):
        if self.length < 1:
            return "<Empty List>"
        ptr = self.head
        final = ""
        while ptr.next is not None:
            final += f" {ptr.value} ->"
            ptr = ptr.next
        final += f" {ptr.value}"
        return final

    # append
    def append(self, node):
        if self.length == 0:
            self.tail = node
            self.head = node
            self.length += 1
            return            
        self.tail.next = node
        self.tail = self.tail.next
        self.length += 1

    def pop(self):
        if self.length <= 1:
            self.head = None
            self.tail = None
            self.length = 0
            return
        ptr = self.head
        while ptr.next != self.tail:
            ptr = ptr.next
        self.tail = ptr
        self.tail.next = None
        self.length -= 1

    def prepend(self, node):
        ptr = self.head
        self.head = node
        self.head.next = ptr
        self.length += 1

    def pop_first(self):
        ptr = self.head
        self.head = self.head.next
        self.length -= 1
        ptr.next = None

    def reverse(self):
        # 5 -> 2 -> 4 -> 6
        # 6 -> 4 -> 2 -> 5
        pass






node = Node(5)
linked_list = LinkedList(node)
node2 = Node(2)
node4 = Node(4)
node6 = Node(6)

linked_list.append(node2)
linked_list.append(node4)
linked_list.append(node6)
print(linked_list)


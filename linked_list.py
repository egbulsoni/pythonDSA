# constructor: node and LL
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

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
            print(ptr.value)
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
        temp = self.head
        self.head = node
        self.head.next = temp
        self.length += 1
        return

    def pop_first(self):
        ptr = self.head
        self.head = self.head.next
        self.length -= 1
        ptr.next = None

    def get(self, pos):
        try:
            temp = self.head
            for i in range(pos):
                temp = temp.next
            print(temp.value)
            return temp
        except:
            print("couldn't find said index.")

    def set(self, pos, value):
        node = self.get(pos)
        if node:
            node.value = value

    def insert(self, pos, node):
        if pos == 0:
            self.prepend(node)
            return
        pre = self.head
        temp = self.head
        for i in range(pos):
            pre = temp
            temp = temp.next
        pre.next = node
        node.next = temp
        
    # def reverse(self):
    #     # 5 -> 2 -> 4 -> 6
    #     # 6 -> 4 -> 2 -> 5
    #     # pointers to manage the reversal
    #     prev = None
    #     current = self.head

    #     # Update the tail to be the current head
    #     self.tail = current

    #     while current:
    #         next_node = current.next # Save the next node
    #         current.next = prev # Reverse the current node's pointer
    #         prev = current # Move 'prev' forward
    #         current = next_node # Move 'current' forward
        
    #     # Update head to be the last node we processed
    #     self.head = prev

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = None
        before = None
        
        # Iterate over the list and reverse the pointers
        for _ in range(self.length):
            after = temp.next  # Save the next node
            temp.next = before  # Reverse the current node's pointer
            before = temp      # Move 'before' forward
            temp = after       # Move 'temp' forward

        
node = Node(5)
linked_list = LinkedList(node)
node2 = Node(2)
node4 = Node(4)
node6 = Node(6)

linked_list.append(node2)
linked_list.append(node4)
linked_list.append(node6)
print(linked_list)

# node7 = Node(7)
# linked_list.prepend(node7)
# print(linked_list)

# # linked_list.pop_first()
# # print(linked_list)
# linked_list.get(4)
# linked_list.set(8,8)
# print(linked_list)

# linked_list.insert(0,Node(15))
# print(linked_list)

linked_list.reverse()
print(linked_list)
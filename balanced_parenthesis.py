class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.length = 0
        self.top = None
        
    def __str__(self):
        ps = ""
        temp = self.top
        for _ in range(self.length):
            ps += str(temp.value) + "->"
            temp = temp.next
        ps += "None"
        return ps
    
    def push(self, node):
        if self.top:
            node.next = self.top 
        self.top = node
        self.length += 1
        
    def pop(self):
        try:
            temp = self.top
            self.top = self.top.next
            self.length -= 1
            return temp
        except:
            print("Error! tried to pop from an empty stack")
            raise Exception("Deu ruim, campeao!")

#n1 = Node(1)
#n2 = Node(2)
#n3 = Node(3)
#s = Stack(n1)
#s.push(n2)
#s.push(n3)
#print(s)
#s.pop()
#print(s)
#rawstr = "()(())"
#rawstr = ")()"
#rawstr = "()))"
rawstr = "()(("
s = Stack()

def validate_parenthesis(rs):
    for c in rs:
        if c == '(':
            s.push(Node(c))
        elif c == ')':
            s.pop()
            
    return s.length == 0
    
if validate_parenthesis(rawstr):
    print("VALID!")
else:
    print("INVALID!!!")
        

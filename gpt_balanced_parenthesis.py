class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Pilha vazia: não é possível desempilhar.")

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return "->".join(map(str, reversed(self.items))) + "->None"


def validate_parenthesis(expression):
    stack = Stack()
    for char in expression:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                print("Erro: parêntese de fechamento sem correspondente.")
                return False
            stack.pop()
    
    if not stack.is_empty():
        print("Erro: parênteses de abertura sobrando.")
        return False
    
    return True


# Testando o código
rawstr = "()(())"  # Tente diferentes entradas, como ")", "(()", etc.
if validate_parenthesis(rawstr):
    print("VALID!")
else:
    print("INVALID!!!")

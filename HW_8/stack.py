class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def push(self, item: float) -> None:
        self.data.append(item)

    def pop(self) -> float:
        if not self.is_empty():
            return self.data.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self) -> float:
        if not self.is_empty():
            return self.data[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self) -> float:
        return len(self.data)


def test_secret_stack():
    stack = Stack()
    assert stack.is_empty() == True
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.size() == 3
    assert stack.peek() == 3
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.size() == 1
    assert stack.is_empty() == False
    assert stack.pop() == 1
    assert stack.is_empty() == True


def first_k_secret_elements(stack, k):
    elements = []
    for _ in range(min(k, stack.size())):
        elements.append(stack.pop())
    return elements


def reverse_string(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)
    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string


def brackets_balance(input_string):
    stack = Stack()
    brackets = {'(': ')', '[': ']', '{': '}'}
    for char in input_string:
        if char in brackets.keys():
            stack.push(char)
        elif char in brackets.values():
            if stack.is_empty() or brackets[stack.pop()] != char:
                return False
    return stack.is_empty()


test_secret_stack()


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(first_k_secret_elements(s, 2))  
print(reverse_string("Melon")) 
print(brackets_balance("{[()]}"))  
print(brackets_balance("{[()}]")) 
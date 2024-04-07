class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)
        print("ok")

    def pop(self):
        print(self.stack.pop())

    def back(self):
        print(self.stack[-1])

    def size(self):
        print(len(self.stack))

    def clear(self):
        self.stack.clear()
        print("ok")

stack = Stack()

while True:
    command = input().split()
    operation = command[0]
    if operation == "push":
        stack.push(int(command[1]))
    elif operation == "pop":
        stack.pop()
    elif operation == "back":
        stack.back()
    elif operation == "size":
        stack.size()
    elif operation == "clear":
        stack.clear()
    elif operation == "exit":
        print("bye")
        break

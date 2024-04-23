class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)
        print("ok")

    def pop(self):
        if self.is_empty():
            print("error")
        else:
            print(self.stack.pop())

    def back(self):
        if self.stack:
            print(self.stack[-1])
        else:
            print('error')


    def size(self):
        print(len(self.stack))

    def clear(self):
        self.stack.clear()
        print("ok")

    def is_empty(self):
        return len(self.stack) == 0

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

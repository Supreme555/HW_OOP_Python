class Queue:
    def __init__(self):
        self.queue = []

    def push(self, n):
        self.queue.append(n)
        print("ok")

    def pop(self):
        if self.is_empty():
            print("error")
        else:
            print(self.queue.pop(0))

    def front(self):
        if self.is_empty():
            print("error")
        else:
            print(self.queue[0])

    def size(self):
        print(len(self.queue))

    def clear(self):
        self.queue.clear()
        print("ok")

    def is_empty(self):
        return len(self.queue) == 0

queue = Queue()

while True:
    command = input().split()
    operation = command[0]
    if operation == "push":
        queue.push(int(command[1]))
    elif operation == "pop":
        queue.pop()
    elif operation == "front":
        queue.front()
    elif operation == "size":
        queue.size()
    elif operation == "clear":
        queue.clear()
    elif operation == "exit":
        print("bye")
        break

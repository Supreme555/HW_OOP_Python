class Queue:
    def __init__(self, max_size: float) -> None:
        self.queue = []
        self.max_size = max_size

    def is_full(self):
        return len(self.queue) >= self.max_size

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        if not self.is_full():
            self.queue.append(item)
        else:
            print("Очередь заполнена, элемент не добавлен.")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Очередь пуста, невозможно выполнить операцию.")

    def size(self):
        return len(self.queue)


def binary_representation(n):
    result = []
    for i in range(1, n+1):
        result.append(bin(i)[2:])
    return result


q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.size()) 


print(binary_representation(4))

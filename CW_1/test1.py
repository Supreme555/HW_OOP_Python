from my_queue import Queue

q = Queue()

q.append(5)
q.append(4)
q.append(6)
q.append(1)
q.append(3)
q.append(2)

# while not q.is_empty():
#     print(q.pop_front())

# def print_first_k(q: Queue, k: int) -> None:
#     while not q.is_empty() and k > 0:
#         print(q.pop_front())
#         k -= 1

# print_first_k(q, 10)

def reversed_queue(q: Queue) -> Queue:
    if q.is_empty():
        return
    x = q.pop_front()
    reversed_queue(q)
    q.append(x)

reversed_queue(q)

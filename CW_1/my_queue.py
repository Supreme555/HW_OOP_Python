from typing import List, Any


class Queue:
    def __init__(self) -> None:
        self.elements: List = []

    def append(self, x) -> None:
        self.elements.append(x)

    def pop_front(self) -> Any:
        if not self.is_empty():
            return self.elements.pop(0)
        return None
    
    def size(self) -> int:
        return len(self.elements)

    def is_empty(self) -> bool:
        return self.elements == []
    
    def peak(self) -> Any:
        if not self.is_empty():
            return self.elements[0]
        return None

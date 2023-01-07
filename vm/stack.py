from collections import deque


class Stack:
    # LIFO  stack
    def __init__(self) -> None:
        self.queue = deque()

    def push(self, val):
        self.queue.append(val)

    def pop(self):
        return self.queue.pop()

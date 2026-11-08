class MyStack:
#using stack make queue
    def __init__(self):
        from collections import deque
        self.q=deque()
        
        

    def push(self, x: int) -> None:
        size=len(self.q)
        self.q.append(x)
        for _ in range(size):
            self.q.append(self.q.popleft())
           #previous elements are moved to the back

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
# This implementation uses a deque to simulate a queue using stack operations.
#
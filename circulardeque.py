class CircularDeque:
    def __init__(self, k: int):
        self.deque = [None] * k
        self.front = 0
        self.rear = 0
        self.size = k
    
    def insertFront(self, val):
        if self.front == self.rear and self.deque[self.front] is not None:
            return False
        
        self.front -= 1
        if self.front == -1:
            self.front = self.size - 1
        self.deque[self.front] = val
        return True
    
    def insertLast(self, val):
        if self.front == self.rear and self.deque[self.front] is not None:
            return False
        
        self.deque[self.rear] = val
        self.rear += 1
        if self.rear == self.size:
            self.rear = 0
        return True
    
    def deleteFront(self):
        if self.front == self.rear and self.deque[self.front] is None:
            return False
        
        self.deque[self.front] = None
        self.front += 1
        if self.front == self.size:
            self.front = 0
        return True
    
    def deleteLast(self):
        if self.front == self.rear and self.deque[self.front] is None:
            return False
        
        self.rear -= 1
        if self.rear == -1:
            self.rear = self.size - 1
        self.deque[self.rear] = None
        return True
    
    def getFront(self):
        if self.deque[self.front] is None:
            return -1
        return self.deque[self.front]
    
    def getLast(self):
        if not self.rear:
            tmp = self.size - 1
        else:
            tmp = self.rear - 1
        
        if self.deque[tmp] is None:
            return -1
        return self.deque[tmp]
    
    def isEmpty(self):
        if self.front == self.rear and self.deque[self.front] is None:
            return True
        return False
    
    def isFull(self):
        if self.front == self.rear and self.deque[self.front] is not None:
            return True
        return False
# 원형 큐 클래스 모듈입니다.

class EmptyQueueError(Exception):
    def __str__(self):
        return 'There is nothing to pop in this queue.'

class CircularQueue:
    def __init__(self, size: int):
        self.q = [None] * size
        self.size = size
        self.front = 0
        self.rear = 0
    
    def enqueue(self, val) -> bool:
        # 큐가 꽉 차 있으면 False 반환
        if self.q[self.front] is not None and self.front == self.rear:
            return False
        self.q[self.rear] = val
        self.rear += 1
        if self.rear == self.size:
            self.rear = 0
        return True
    
    def dequeue(self):
        # 큐가 비어있으면 에러 출력
        if self.q[self.front] is None:
            raise EmptyQueueError
        value = self.q[self.front]
        self.q[self.front] = None
        self.front += 1
        if self.front == self.size:
            self.front = 0
        return value
<span style='font-family: Consolas'>

## 스택, Stack
&nbsp;후입선출(LIFO, Last-In-First-Out)의 방식으로 작동하며, 다음의 두 가지 주요 연산을 지원하는 추상 자료형이다.

1. push(): 요소를 컬렉션에 추가한다.
2. pop(): 가장 최근에 삽입된 요소를 제거한다.

&nbsp;파이썬에서는 데크(deque) 자료형을 이용하여 효율적으로 사용 가능하다.
```python
from collections import deque
stack = deque()
```

### 연결 리스트를 이용한 스택 ADT 구현

```python
# 연결 리스트 정의
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

# 스택 정의
class Stack:
    def __init__(self):
        self.last = None
    
    def push(self, val):
        self.last = Node(val, self.last)
    
    def pop(self):
        value = self.last.val
        self.last = self.last.next
        return value
```
<br/><br/>

## 큐, Queue
&nbsp;선입선출(FIFO, First-In-First-Out)로 처리되는, 한쪽 끝에는 요소를 추가하고 반대쪽 끝에는 요소를 제거할 수 있는 추상 자료형이다.

### 큐를 이용한 스택 구현
```python
class Stack:
    def __init__(self):
        self.q = collections.deque()
    
    def push(self, val):
        self.q.append(val)
    
    def pop(self):
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        return self.q.popleft()
```

### 스택을 이용한 큐 구현
```python
class Queue:
    def __init__(self):
        self.s = collections.deque()
    
    def push(self, val):
        self.s.append(val)
    
    # 스택 두 개 사용
    def pop(self):
        tmp = collections.deque()
        for _ in range(len(self.s) - 1):
            tmp.append(self.s.pop())
        value = self.s.pop()
        while tmp:
            self.s.append(tmp.pop())
        return value
```

### 원형 큐 디자인
```python
class EmptyQueueError(Exception):
    def __str__(self):
        return 'There is nothing to pop in this queue.'

class CircularQueue:
    def __init__(self, size: int):
        self.q = [None] * size
        self.size = size
        self.front = 0
        self.rear = 0
    
    # enqueue(): rear 포인터 이동
    def enqueue(self, val) -> bool:
        # 큐가 꽉 차 있으면 False 반환
        if self.q[self.front] is not None and self.front == self.rear:
            return False
        self.q[self.rear] = val
        self.rear += 1
        if self.rear == self.size:
            self.rear = 0
        return True
    
    # dequeue(): front 포인터 이동
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

```
<br/><br/><br/>

## 데크, Deque
- **Double-Ended Queue**의 줄임말로, 양쪽 끝에서 요소를 추출할 수 있는 형태의 추상 자료형이다.

- 일반적으로 이중 연결 리스트로 구현한다.

### 원형 데크 디자인
```python
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
```
<br/><br/>

## 우선순위 큐, Priority Queue
&nbsp;스택이나 큐와 다르게, 각 요소의 우선순위에 따라 추출된다.
힙(heap) 자료구조와 연관이 크다.



class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        self.queue.pop(0)





string = 'my string'
string1 = 'another string'
Q = Queue()
Q.enqueue(string)
print(Q.queue)
Q.enqueue(string1)
print(Q.queue)
Q.dequeue()
print(Q.queue)


from LinkedList import LinkedListElement

class Queue():
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        empty = False
        if self.head is None:
            empty = True
        return empty
    
    def enqueue(self, value):
        element = LinkedListElement(value)
        if self.is_empty():
            self.head = element
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = element
        return
    
    def dequeue(self):
        dequeued_value = None
        if not self.is_empty():
            dequeued_value = self.head.value
            temp = self.head
            self.head = self.head.next
            del temp
        return dequeued_value

def main():
    q = Queue()
    print("Created an empty Queue!")
    print("Enqueue 1.")
    q.enqueue(1)
    print("Enqueue 2.")
    q.enqueue(2)
    print("Enqueue 3.")
    q.enqueue(3)
    print("Enqueue 4.")
    q.enqueue(4)
    print("Enqueue 5.")
    q.enqueue(5)
    print("Dequeue returned {} value.".format(q.dequeue()))
    print("Dequeue returned {} value.".format(q.dequeue()))
    print("Dequeue returned {} value.".format(q.dequeue()))
    print("Dequeue returned {} value.".format(q.dequeue()))
    print("Dequeue returned {} value.".format(q.dequeue()))
    print("Dequeue returned {} value.".format(q.dequeue()))

"""
Uncomment the following line to run the file.
"""
#main()
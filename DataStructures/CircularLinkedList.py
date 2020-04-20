from LinkedList import LinkedListElement

class CircularLinkedList():
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        empty = False
        if self.head is None:
            empty = True
        return empty
    
    def add(self, value):
        element = LinkedListElement(value)
        if self.is_empty():
            self.head = element
            self.head.next = self.head
        else:
            temp = self.head
            # Finding the last node
            while temp.next != self.head:
                temp = temp.next
            temp.next = element
            element.next = self.head
        return
    
    def delete(self, value):
        deleted = False
        if not self.is_empty():
            if self.head.next == self.head:
                # There is only one element
                if self.head.value == value:
                    temp = self.head
                    self.head = None
                    del temp
                    deleted = True
            else:
                # Checking at head
                if self.head.value == value:
                    last = self.head
                    while last.next != self.head:
                        last = last.next
                    temp = self.head
                    last.next = self.head.next
                    self.head = last.next
                    del temp
                    deleted = True
                else:
                    prev = self.head
                    current = self.head.next
                    while current.next != self.head:
                        if current.value == value:
                            temp = current
                            prev.next = current.next
                            del temp
                            deleted = True
                            break
                        prev = current
                        current = current.next
                    if not deleted:
                        # Checking for last
                        last = current
                        if last.value == value:
                            prev.next = self.head
                            del last
                            deleted = True
        return deleted
    
    def traverse(self):
        s = ""
        temp = self.head
        while temp.next != self.head:
            s += str(temp.value) + "->"
            temp = temp.next
        s += str(temp.value)
        print(s)
        return

def main():
    cll = CircularLinkedList()
    print("Created an empty Circular Linked List!")
    print("Adding 1.")
    cll.add(1)
    print("Circular Linked list looks as follows:")
    cll.traverse()
    print("Adding 2.")
    cll.add(2)
    print("Circular Linked list looks as follows:")
    cll.traverse()
    print("Adding 3.")
    cll.add(3)
    print("Adding 4.")
    cll.add(4)
    print("Adding 5.")
    cll.add(5)
    print("Circular Linked list looks as follows:")
    cll.traverse()
    print("Removing 3.")
    cll.delete(3)
    print("Circular Linked list looks as follows:")
    cll.traverse()
    print("Removing 4.")
    cll.delete(4)
    print("Circular Linked list looks as follows:")
    cll.traverse()
    print("Removing 1.")
    cll.delete(1)
    print("Circular Linked list looks as follows:")
    cll.traverse()

"""
Uncomment the following line to run the file.
"""
#main()
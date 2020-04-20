class LinkedListElement():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
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
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = element
        return
    
    def delete(self, value):
        deleted = False
        if not self.is_empty():
            if self.head.value == value:
                temp = self.head
                self.head = self.head.next
                del temp
                deleted = True
            if not deleted and self.head.next is not None:
                prev = self.head
                current = self.head.next
                while current is not None:
                    if current.value == value:
                        prev.next = current.next
                        del current
                        deleted = True
                        break
                    prev = current
                    current = current.next
        return deleted
    
    def traverse(self):
        s = ""
        temp = self.head
        while temp is not None:
            s += str(temp.value)
            temp = temp.next
            if temp is not None:
                s += "->"
        print(s)
        return

def main():
    ll = LinkedList()
    print("Created an empty Linked List!")
    print("Adding 1.")
    ll.add(1)
    print("Linked list looks as follows:")
    ll.traverse()
    print("Adding 2.")
    ll.add(2)
    print("Linked list looks as follows:")
    ll.traverse()
    print("Adding 3.")
    ll.add(3)
    print("Adding 4.")
    ll.add(4)
    print("Adding 5.")
    ll.add(5)
    print("Linked list looks as follows:")
    ll.traverse()
    print("Removing 3.")
    ll.delete(3)
    print("Linked list looks as follows:")
    ll.traverse()
    print("Removing 4.")
    ll.delete(4)
    print("Linked list looks as follows:")
    ll.traverse()
    print("Removing 1.")
    ll.delete(1)
    print("Linked list looks as follows:")
    ll.traverse()

"""
Uncomment the following line to run the file.
"""
#main()
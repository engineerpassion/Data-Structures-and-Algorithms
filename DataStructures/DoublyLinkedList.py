class DoublyLinkedListElement():
    def __init__(self, value):
        self.value = value
        self.prev = self.next = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        empty = False
        if self.head == self.tail == None:
            empty = True
        return empty
    
    def add(self, value):
        element = DoublyLinkedListElement(value)
        if self.is_empty():
            self.head = element
            self.tail = element
        else:
            self.tail.next = element
            element.prev = self.tail
            self.tail = element
        return
    
    def delete(self, value):
        deleted = False
        if not self.is_empty():
            if self.head == self.tail:
                if self.head.value == value:
                    # There is only one element
                    temp = self.head
                    self.head = self.tail = None
                    del temp
                    deleted = True
            else:
                # Checking on head
                if self.head.value == value:
                    temp = self.head
                    self.head = self.head.next
                    self.head.prev = None
                    del temp
                    deleted = True
                # Checking on tail
                elif self.tail.value == value:
                    temp = self.tail
                    self.tail = self.tail.prev
                    self.tail.next = None
                    del temp
                    deleted = True
                # Checking on the rest of the Doubly Linked List
                else:
                    temp = self.head.next
                    while temp is not None:
                        if temp.value == value:
                            temp_prev = temp.prev
                            temp_next = temp.next
                            temp_prev.next = temp_next
                            temp_next.prev = temp_prev
                            del temp
                            deleted = True
                            break
                        temp = temp.next
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
    dl = DoublyLinkedList()
    print("Created an empty Doubly Linked List!")
    print("Adding 1.")
    dl.add(1)
    print("Doubly Linked list looks as follows:")
    dl.traverse()
    print("Adding 2.")
    dl.add(2)
    print("Doubly Linked list looks as follows:")
    dl.traverse()
    print("Adding 3.")
    dl.add(3)
    print("Adding 4.")
    dl.add(4)
    print("Adding 5.")
    dl.add(5)
    print("Doubly Linked list looks as follows:")
    dl.traverse()
    print("Removing 3.")
    dl.delete(3)
    print("Doubly Linked list looks as follows:")
    dl.traverse()
    print("Removing 4.")
    dl.delete(4)
    print("Doubly Linked list looks as follows:")
    dl.traverse()
    print("Removing 1.")
    dl.delete(1)
    print("Doubly Linked list looks as follows:")
    dl.traverse()

"""
Uncomment the following line to run the file.
"""
#main()
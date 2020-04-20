from DoublyLinkedList import DoublyLinkedListElement

class DoublyCircularLinkedList():
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
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            self.tail.next = element
            element.prev = self.tail
            element.next = self.head
            self.head.prev = element
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
                    self.head.prev = self.tail
                    self.tail.next = self.head
                    del temp
                    deleted = True
                # Checking on tail
                elif self.tail.value == value:
                    temp = self.tail
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
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
        while temp.next != self.head:
            s += str(temp.value) + "->"
            temp = temp.next
        s += str(temp.value)
        print(s)
        return

def main():
    dcll = DoublyCircularLinkedList()
    print("Created an empty Doubly Circular Linked List!")
    print("Adding 1.")
    dcll.add(1)
    print("Doubly Circular Linked list looks as follows:")
    dcll.traverse()
    print("Adding 2.")
    dcll.add(2)
    print("Doubly Circular Linked list looks as follows:")
    dcll.traverse()
    print("Adding 3.")
    dcll.add(3)
    print("Adding 4.")
    dcll.add(4)
    print("Adding 5.")
    dcll.add(5)
    print("Doubly Circular Linked list looks as follows:")
    dcll.traverse()
    print("Removing 3.")
    dcll.delete(3)
    print("Doubly Circular Linked list looks as follows:")
    dcll.traverse()
    print("Removing 4.")
    dcll.delete(4)
    print("Doubly Circular Linked list looks as follows:")
    dcll.traverse()
    print("Removing 1.")
    dcll.delete(1)
    print("Doubly Circular Linked list looks as follows:")
    dcll.traverse()

"""
Uncomment the following line to run the file.
"""
#main()
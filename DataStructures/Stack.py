from LinkedList import LinkedListElement

class Stack():
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        empty = False
        if self.top is None:
            empty = True
        return empty
    
    def push(self, value):
        element = LinkedListElement(value)
        if self.is_empty():
            self.top = element
        else:
            element.next = self.top
            self.top = element
        return
    
    def pop(self):
        popped_value = None
        if not self.is_empty():
            popped_value = self.top.value
            temp = self.top
            self.top = self.top.next
            del temp
        return popped_value

def main():
    s = Stack()
    print("Created an empty Stack!")
    print("Push 1.")
    s.push(1)
    print("Push 2.")
    s.push(2)
    print("Push 3.")
    s.push(3)
    print("Push 4.")
    s.push(4)
    print("Push 5.")
    s.push(5)
    print("Pop returned {} value.".format(s.pop()))
    print("Pop returned {} value.".format(s.pop()))
    print("Pop returned {} value.".format(s.pop()))
    print("Pop returned {} value.".format(s.pop()))
    print("Pop returned {} value.".format(s.pop()))
    print("Pop returned {} value.".format(s.pop()))

"""
Uncomment the following line to run the file.
"""
#main()
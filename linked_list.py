class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node.
    """

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = None



class LinkedList:
    """
     Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current.data
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        current = self.head
        position = index
        if index == 0:
            self.add(data)
        else:
            while position > 1:
                position -= 1
                current = current.next_node
            new_node = Node(data)
            prev_node = current
            next_node = current.next_node
            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self, data):
        current = self.head
        prev = None
        found = False

        while current and not found:
            if current.data == data and current is self.head:
                self.head = current.next_node
                found = True
            elif current.data == data:
                prev.next_node = current.next_node
                found = True
            else:
                prev = current
                current = current.next_node
     #   return current



    def __repr__(self):

        current = self.head
        if current is None:
            print("Empty List!!!")
            return False

        while current:
            #print(str(start.get_data()), end=" ")
            print(str(current.data), end=" ")

            current = current.next_node
            if current:
                print("-->", end=" ")
            else:
                print("--> Null", end=" ")
        print()


l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(10)
l.__repr__()
l.insert(20, 3)
l.__repr__()
l.remove(2)
l.__repr__()




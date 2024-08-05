class Node():
    def __init__(self, data=None, next=None):
        self.data= data
        self.next= next


class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        iterator = self.head

        while iterator:
            if iterator.next is None:
                node = Node(data, None)
                iterator.next= node
                return
            else:
                iterator = iterator.next

    def print_linkedlist(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        iterator = self.head
        llist = ''
        while iterator:
            llist += str(iterator.data) + '-->'
            iterator = iterator.next

        print(llist)


if __name__ == '__main__':
    LL = LinkedList()
    LL.insert_at_begining(24)
    LL.insert_at_begining(23)
    LL.insert_at_begining(22)
    LL.insert_at_end(25)
    LL.insert_at_end(26)
    LL.insert_at_end(27)
    LL.print_linkedlist()
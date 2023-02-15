#write your own basic LinkedList class. You should at 
#least be able to add an item, remove an item. 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_item(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def remove_item(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None and current.next.data != data:
            current = current.next

        if current.next is not None:
            current.next = current.next.next

    def __str__(self):
        items = []
        current = self.head
        while current is not None:
            items.append(str(current.data))
            current = current.next
        return "->".join(items)

my_list = LinkedList()

my_list.add_item(1)
my_list.add_item(2)
my_list.add_item(3)
my_list.add_item(4)
print(my_list)  # should print "1->2->3->4"

my_list.remove_item(2)

print(my_list)  # should print "1->3"

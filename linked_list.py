class Node:
    def __init__(self, head):
        self.head = head
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

# 1 --> 2 --> 3 --> 4 --> Null


def display_linked_list1(current):
    while current:
        print(current.head)
        current = current.next


display_linked_list1(a)


# using recursion

def display_linked_list2(current):
    if not current:
        return
    print(current.head, end=' --> ')
    display_linked_list2(current.next)


display_linked_list2(a)





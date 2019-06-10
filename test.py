from day1 import middle_node

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def initialize_list():
    list_node = Node(1)
    head = list_node
    list_node.next = Node(2)
    list_node.next.next = Node(3)
    list_node.next.next.next = Node(4)
    list_node.next.next.next.next = Node(5)
    list_node.next.next.next.next.next = Node(6)
    return (head, list_node)

if __name__== '__main__':
    list_node = initialize_list()

    print(middle_node(list_node[0], list_node[1]))

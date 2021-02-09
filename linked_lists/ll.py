

"""
Notes

Watch the termination of your while loop

- Difference between while node: & while node.next:
    - One leaves current node at None and the other stops at last node

The trick is understanding what you are trying to do (just traverse, append node, etc).
Based on this, you can determine where to terminate the loop (if at last node or past it)


"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


#init nodes
root = Node(0)
first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

#init links
root.next = first
first.next = second
second.next = third
third.next = fourth
fourth.next = fifth



#traverse ll
def traverse(root):
    while root:
        print(root.val)
        root = root.next


#insert end
def insert_end(root, new_node):
    dummy = Node(-1)
    dummy.next = root

    #traverse and place at end
    while dummy.next:
        dummy = dummy.next
    dummy.next = new_node

    #to confirm, print new ll
    while root:
        print(root.val)
        root = root.next


#insert beginning
def insert_beginning(root, new_node):
    dummy = Node(-1)
    dummy.next = new_node
    new_node.next = root

    while new_node:
        print(new_node.val)
        new_node = new_node.next


# traverse(root)
# insert_end(root, fifth)
# insert_beginning(root, fifth)

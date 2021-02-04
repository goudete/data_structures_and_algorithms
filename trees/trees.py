
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

#root
root = Node(1)

#2nd gen
root_left = Node(2)
root_right = Node(3)

#3rd gen
third_left = Node(4)
third_right = Node(5)
third_left_r = Node(6)
third_right_r = Node(7)

#connecting tree
root.left = root_left
root.right = root_right
root_left.left = third_left
root_left.right = third_right
root_right.left = third_left_r
root_right.right = third_right_r


def dfs_pre_order(root):
    if root:
        print(root.val)
        dfs_pre_order(root.left)
        dfs_pre_order(root.right)


def dfs_in_order(root):
    if root:
        dfs_in_order(root.left)
        print(root.val)
        dfs_in_order(root.right)


def dfs_post_order(root):
    if root:
        dfs_post_order(root.left)
        dfs_post_order(root.right)
        print(root.val)

def bfs(root):
    q = []
    q.append(root)
    while q:
        node = q.pop(0)
        print(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


print("Pre Order")
dfs_pre_order(root)
print(' ')

print('In Order')
dfs_in_order(root)
print(' ')

print("Post Order")
dfs_post_order(root)

print("BFS")
bfs(root)

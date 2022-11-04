class Node:
    def __init__(self,data,left_node,right_node):
        self.data=data
        self.left_node=left_node
        self.right_node=right_node

#전위순회(Preorder Traversal)
def pre_order(node):
    print(node.data,end=' ')
    if node.left_node!=None:
        pre_order(tree[node.left_node])
    if node.right_node!=None:
        pre_order(tree[node.right_node])

#중위순회(Inorder Traversal)
def in_order(node):   
    if node.left_node!=None:
        in_order(tree[node.left_node])
    print(node.data,end=' ')
    if node.right_node!=None:
        in_order(tree[node.right_node])

#후위순회(Postorder Traversal)
def post_order(node):
    if node.left_node!=None:
        post_order(tree[node.left_node])
    if node.right_node!=None:
        post_order(tree[node.right_node])
    print(node.data,end=' ')

n=int(input())
tree={}

for i in range(n):
    data,left_node,right_node=input().split()
    if left_node=="None":
        left_Node=None
    if right_node=="None":
        right_node=None
    tree[data]=Node(data,left_node,right_node)
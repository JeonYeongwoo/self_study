# gpt 이용해서 탐색 알고리즘 구현함.
# 후일 다시 구현하여 재풀이할 것.
# 백준에 제출 x

class Node:
    def __init__(self, item=None):
        self.item = item
        self.left = None
        self.right = None
        
class tree:
    def __init__(self, item = None):
        self.root = None
        
t = tree()
        
# 전위 순회 : root -> left -> right 
def preorder(N):
    print(N.item, end="")
    if (N.left != None):
        preorder(N.left)
    if (N.right != None):
        preorder(N.right)
    
    
# 중위 순회 : left -> root -> right 
def inorder(N):
    if (N.left != None):
        inorder(N.left)
    print(N.item, end="")
    if (N.right != None):
        inorder(N.right)
    

# 후위 순회 : left -> right -> root
def postorder(N):
    if (N.left != None):
        postorder(N.left)
    if (N.right != None):
        postorder(N.right)
    print(N.item, end="")
    

def search (item, N):
        # ===== 시도 1 - 실패 =======
        # if (item == N.item):
        #     print(N.item)
        #     return N
        # if (N.left != None):
        #     # search(item, N.left)
        #     return search(item, N.left)
        # if (N.right != None):
        #     return search(item, N.right)
        #
        # 이유 : N.left가 있으면 무조건 왼쪽으로 return 해버림
        #       그래서 왼쪽에서 못 찾았을 때 오른쪽으로 넘어갈 기회가 없음
        #============================
        
        # 지피티 통한 답
        if N is None: # root = None 으로 전달될 때 고려
            return None
        
        
        found = search(item, N.left)
        if (found != None):
            return found
        
        if (item == N.item):
            print(N.item)
            return N
        
        
        return search(item, N.right)


def insert(parent, left, right):
    global t;

    if (t.root == None):
        t.root = Node(parent)
        
    N = search(parent, t.root)
    
    if (left == '.'):
        N.left = None
    else:
        N.left = Node(left)
        
    if (right == '.'):
        N.right = None
    else:
        N.right = Node(right)
    

N = int(input())

for i in range(N):
    inp = input().split()
    insert(inp[0], inp[1], inp[2])
    
preorder(t.root)
print()
inorder(t.root)
print()
postorder(t.root)
    
    
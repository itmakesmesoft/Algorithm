'''
test case

7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
'''

def preorder(now):
    if now !='.':
        print(now, end='')
        preorder(edge[now][0])
        preorder(edge[now][1])

def inorder(now):
    if now !='.':
        inorder(edge[now][0])
        print(now, end='')
        inorder(edge[now][1])
        
def postorder(now):
    if now !='.':
        postorder(edge[now][0])
        postorder(edge[now][1])
        print(now, end='')
        

n = int(input())
edge = {}
for i in range(1, n+1):
    lst = list(input().split())
    edge[lst[0]] = lst[1:]
preorder('A')
print()
inorder('A')
print()
postorder('A')
"""
1. 코드설명
기본적으로 TNode 클래스는 매개변수로 값, 왼쪽 링크, 오른쪽 링크를 받아 객체를 생성한다.
전위 순회는 해당 노드를 방문한 후에(n.print) 왼쪽 노드를 모두 방문하고(binary_tree[n.left]) 오른쪽 노드를 모두 방문한다(binary_tree[n.right])
중위 순회는 왼쪽 노드를 모두 방문하고 마지막 노드의 해당 노드를 방문한 후에 오른쪽 노드를 모두 방문한다
후위 순회는 왼쪽, 오른쪽 노드를 모두 방문하고 마지막에 해당 노드를 방문한다.
횟수를 변수 num에 담고 횟수만큼 받은 item, left ,right 값을 리스트에 저장한다.
리스트에 저장된 값의 item을 key값으로 받고 left, right값을 value로 받는 딕셔너리를 생성한 후에
전위,중위,후위 순회에 해당 딕셔너리를 연결하여 코드를 제작했다

2. 시간복잡도
기본연산을 print(n.data)로 했을때의 시간복잡도는
T(n) = n
"""
import time
start = time.time()

# 이진트리를 위한 노드 클래스
class TNode:
    def __init__ (self, data, left, right):	# 생성자
        self.data = data 			# 노드의 데이터
        self.left = left			# 왼쪽 자식을 위한 링크
        self.right = right			# 오른쪽 자식을 위한 링크

# 1번을 해보세요!
#전위 순회
def preorder(n) :
    print(n.data,end=' ')
    if binary_tree[n.data].left != '-1': # 딕셔너리의 key값의 왼쪽이 -1이면 검색 종료
        preorder(binary_tree[n.left])
    if binary_tree[n.data].right != '-1': # 딕셔너리의 key값의 오른쪽이 -1이면 검색 종료
        preorder(binary_tree[n.right])

#중위 순회
def inorder(n) :
    if binary_tree[n.data].left != '-1': # 딕셔너리의 key값의 왼쪽이 -1이면 검색 종료
        preorder(binary_tree[n.left])
    print(n.data,end=' ')
    if binary_tree[n.data].right != '-1': # 딕셔너리의 key값의 오른쪽이 -1이면 검색 종료
        preorder(binary_tree[n.right])

#후위 순회
def postorder(n) :
    if binary_tree[n.data].left != '-1': # 딕셔너리의 key값의 왼쪽이 -1이면 검색 종료
        preorder(binary_tree[n.left])
    if binary_tree[n.data].right != '-1': # 딕셔너리의 key값의 오른쪽이 -1이면 검색 종료
        preorder(binary_tree[n.right])
    print(n.data,end=' ')


# 2번을 해보세요!
num = int(input())
inputs = []

for i in range(num):
    inputs.append(input().split())

binary_tree = {} # 딕셔너리로 binary_tree 생성. 노드들의 연결을 딕셔너리의 key값으로 찾기 용이하기 때문
for item, left, right in inputs:
    binary_tree[item] = TNode(item, left, right)

# 출력합니다!
root = binary_tree['1']
print('Pre-Order : ', end='')
preorder(root)
print()
print('In-Order : ', end='')
inorder(root)
print()
print('Post-Order : ', end='')
postorder(root)
print()
print('실행시간:',time.time()-start)
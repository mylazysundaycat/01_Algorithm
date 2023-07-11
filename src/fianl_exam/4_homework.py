import copy, math, queue
import numpy as np
from queue import  Queue
#문자열 매칭문제
def string_matching(T, P):
    n = len(T)
    m = len(P)
    for i in range(n-m+1):
        j = 0
        while j<m and P[j]==T[i+j]:
            j += 1
            if j == m:
                return i
    return -1

#최근접 쌍의 거리 문제
def closest_pair(p):
    n = len(p)
    min = float("inf")
    for i in range(n-1):
        for j in range(i+1, n):
            dist = math.sqrt((p[i][0]-p[j][0])**2+(p[i][1]-p[j][1])**2)
            if dist < min:
                min = dist
    return min

#Chapter3
#깊이우선탐색 DFS
def dfs(graph, start, visited):
    if start not in visited:
        visited.add(start)
        print(start, end=' ')
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)
mygraph = dict()
e = int(input())
for _ in range(e):
    u, v = input().split()
    if u in mygraph: mygraph[u].add(v)
    else: mygraph[u] = set([v])
    if v in mygraph: mygraph[v].add(u)
    else: mygraph[v] = set([u])
print('DFS : ', end='')
dfs(mygraph, "A", set())
print()

#너비우선탐색 BFS
def bfs(graph, start):
    visited = {start}
    que = queue.Queue()
    que.put(start)
    while not que.empty():
        v = que.get()
        print(v, end=' ')
        nbr = graph[v] - visited
        for u in nbr:
            visited.add(u)
            que.put(u)


#Chatper4
#이진탐색 알고리즘
def binary_search(A, key, low, high) :
    if(low<high): #탐색범위 안에 항목들이 남아있다면
        mid=(low+high)//2
        if key == A[mid]: # 키값과 리스트 안의 인덱스의 값이 같다면
            return mid #중간값이 바로 키값이라면
        elif key < A[mid]:
            return binary_search(A, key, low, mid-1) # 키값이 해당 인덱스 값보다 작아서 왼쪽리스트 탐색
        else:
            return binary_search(A, key, mid+1, high) # 키값이 해당 인덱스 값보다 커서 오른쪽 리스트 탐색
    return -1
def binary_search_iter(A, key, low, high) :
    while(low<=high): #탐색범위 안에 항목이 남아있다면
        mid = (low+high)//2
        if key == A[mid]:
            return mid #탐색 성공! 중간값이 키값일때
        elif key>A[mid]: #키값이 mid값보다 커서 오른쪽에 있을때
            low = mid+1
        else: #키값이 mid값보다 작아서 왼쪽에 있을때
            high = mid-1
    return -1

#Chapter5
#이진트리탐색 알고리즘
class TNode:
    def __init__ (self, data, left, right):	# 생성자
        self.data = data 			# 노드의 데이터
        self.left = left			# 왼쪽 자식을 위한 링크
        self.right = right
def preorder(n):
            print(n.data, end=' ')
            if binary_tree[n.data].left != '-1':  # 딕셔너리의 key값의 왼쪽이 -1이면 검색 종료
                preorder(binary_tree[n.left])
            if binary_tree[n.data].right != '-1':  # 딕셔너리의 key값의 오른쪽이 -1이면 검색 종료
                preorder(binary_tree[n.right])
num = int(input())
inputs = []
for i in range(num):
    inputs.append(input().split())
binary_tree = {} # 딕셔너리로 binary_tree 생성. 노드들의 연결을 딕셔너리의 key값으로 찾기 용이하기 때문
for item, left, right in inputs:
    binary_tree[item] = TNode(item, left, right)

#Chapter6
#기수정렬 알고리즘
BUCKETS = 10 #진수
DIGITS  = 4 #자릿수

def radix_sort(A) :
    queues = []
    for i in range(BUCKETS):
        queues.append(Queue())

    n = len(A)
    factor = 1
    for d in range(DIGITS):
        for i in range(n):
            queues[(A[i]//factor)%10].put(A[i])
        j = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[j] = queues[b].get()
                j += 1
        factor *= 10
        print("step", d+1, A)

#호스풀 알고리즘
NO_OF_CHARS = 128
def shift_table(pat):
    m = len(pat)
    tbl = [m]*NO_OF_CHARS
    for i in range(m-1):
        tbl[ord(pat[i])] = m-1-i
    return tbl
def search_horspool(T, P):
    m = len(P)
    n = len(T)
    t = shift_table(P)
    i = m-1
    while(i<=n-1):
        k=0
        while k<= m-1 and P[m-1-k]==T[i-k]:
            k += 1
        if k==m:
            return i-m+1
        else:
            i+=t[ord(T[i])]
    return -1


#Chapter7
#최장 공통 부분 순서 LCS
def lcs_recur(X,Y,m,n):
    if m==0 or n==0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs_recur(X,Y,m-1,n-1)
    else:
        return max(lcs_recur(X,Y,m,n-1), lcs_recur(X,Y,m-1,n))
def lcs_dp(X,Y):
    m = len(X)
    n = len(Y)
    L = [[None]*(n+1)for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = 1+ L[i-1][j-1]
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    print("LCS = ", lcs_dp_traceback(X, Y, L))
    return L[m][n]

def lcs_dp_traceback(X, Y, L):
    lcs = ""
    i = len(X)
    j = len(Y)

    while i>0 and j>0:
        v = L[i][j]
        if v>L[i][j-1] and v>L[i-1][j] and v>L[i-1][j-1]:
            i -= 1
            j -= 1
            lcs = X[i] + lcs
        elif v == L[i][j-1] and v>L[i-1][j]:
            j -= 1
        else:
            i -= 1
    return lcs


#배낭채우기 정렬 알고리즘
"""
기반상황: 배낭의 무게 = 0, 물건의 갯수 = 0 이면  가치 =0
일반상황: k번째 물건이 배낭의 무게보다 클 때 / k번째 물건이 배낭의 무게보다 작을 때
"""
def knapSack_bf(W, wt, val, n):
        if W==0 or n==0:
            return 0
        elif wt[n-1]>W: # n번재 항목이 배낭 용량보다 크다면
            return knapSack_bf(W, wt, val, n-1)
        else:
            valWith = val[n-1] + knapSack_bf(W-wt[n-1], wt, val, n-1)
            valWithOut = knapSack_bf(W, wt, val, n-1)
            return max(valWith, valWithOut)

def knapSack_dp(W, wt, val, n):
    A = [[0 for x in range(n+1)]for x in range(W+1)]

    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1]> j:
                A[i][j] = A[i-1][j]
            else:
                valWith = val[i-1] + A[i-1][j-wt[i-1]]
                valWithOut = A[i-1][j]
                A[i][j] = max(valWith, valWithOut)
    return A[n][W]

#편집거리
"""
기반상황: 두 문자열 중 하나가 공백일 떄
일반상황: 마지막 문자가 같은 경우 / 같지 않은 경우
"""
def edit_distance(S, T, m, n):
    if m == 0: return n
    if n == 0: return m

    if S[m-1] == T[n-1]: return edit_distance(S, T, m-1, n-1)

    return 1 + min(edit_distance(S, T, m, n-1),
                   edit_distance(S, T, m-1, n),
                   edit_distance(S, T, m-1, n-1))

S = "tuesday"
T = "thursday"
m = len(S)
n = len(T)
mem = [[None for _ in range(n)]for _ in range(m) ]

def edit_distance_mem(S, T, m, n, mem): #알고리즘7.12
    if m == 0: return n
    if n == 0: return m

    if mem[m-1][n-1] == None:
        if S[m-1]==T[n-1]:
            mem[m-1][n-1] = edit_distance_mem(S,T,m-1,n-1,mem)
        else:
            mem[m-1][n-1] = 1 + min(edit_distance_mem(S,T,m,n-1,mem),
                                    edit_distance_mem(S,T,m-1,n,mem),
                                    edit_distance_mem(S,T,m-1,n-1,mem))
        print("mem[%d][%d]=" % (m - 1, n - 1), mem[m - 1][n - 1])
        return mem[m-1][n-1]

#편집거리 예제
def edit_distance_mem2(S, T, m, n, mem):
    if m == 0: return n
    if n == 0: return m

    if mem[m-1][n-1] == None:
        if S[m-1] == T[n-1]:
            mem[m-1][n-1] = edit_distance_mem2(S, T, m-1, n-1, mem)
        else:
            insert = edit_distance_mem2(S, T, m, n-1, mem)
            delete = edit_distance_mem2(S, T, m-1, n, mem)
            replace = edit_distance_mem2(S, T, m-1, n-1, mem)

            min_val = min(insert, delete, replace)

            if min_val == insert:
                print("Insert '%s' at position %d" % (T[n-1], m))
                mem[m-1][n-1] = 1 + insert
            elif min_val == delete:
                print("Delete '%s' at position %d" % (S[m-1], m))
                mem[m-1][n-1] = 1 + delete
            else:
                print("Replace '%s' at position %d with '%s'" % (S[m-1], m, T[n-1]))
                mem[m-1][n-1] = 1 + replace

    return mem[m-1][n-1]


#Chapter8

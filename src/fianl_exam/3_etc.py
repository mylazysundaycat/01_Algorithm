import math
import queue

# 문자열 매칭 [3.3 억지기법]
"""
길이가 n인 입력 문자열 T와
길이가 m인 패턴 문자열 P가 있다.
T에서 가장 먼저 나타나는 P의 위치를 찾아라.
패턴이 없으면 -1을 반환한다
"""
def string_matching(T, P):
    n = len(T)
    m = len(P)
    for i in range(n-m+1):
        j=0
        while j<m and P[i]==T[i+j]:
            j = j+1
            if j==m:
                return 1
    return -1



# 최근접 쌍의 거리 [3.4 억지기법]
"""
가능한 모든 점의 쌍(Pi,Pj)에 대해서 거리를 게산하고 가장 짧은 것을 찾는다
"""
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
def closest_pair(p):
    n = len(p)
    mindist = float("inf")
    for i in range(n-1):
        for j in range(i+1, n):
            if distance(p[i],p[j])<=mindist:
                mindist = distance(p[i],p[j])
    return mindist



# 그래프 탐색 [3.6]
"""
1. 그래프
정점과 간선으로 이루어진 자료구조의 일종 G = (V,E)

2. 깊이 우선 탐색 DFS
미로를 탐색할 때 갈수있을 때 까지 가다가 더 이상 갈 수 없게 되면
다시 가장 가까운 갈림길로 되돌아와서 다른 방향을 다시 탐색하는 전략

3. 너비 우선 탐색 BFS
시작 정점으로부터 인접 정점부터 방문하는 순회 방법

집합 자료형
s1 = set([1,2,3])
s1 = set("123")
s1 = {1,2,3}
s1 = set()
- 중복을 허용하지 않음
- 순서가 없음
s1. add(4) 값 1개 추가
s1. remove(2) 특정 값 삭제

"""
# DFS
def dfs(graph, start, visited): # start는 현재 정점, visited는 집합
    if start not in visited:
        visited.add(start)
        print(start, end=' ')
        nbr = graph[start]-visited
        for v in nbr:
            dfs(graph, v, visited)
# BFS
def bfs(graph, start):
    visited = {start} # 현재정점 start만 방문한 정점임
    que = queue.Queue()
    que.put(start)
    while not que.empty():
        v = que.get() # 큐에서 하나의 정점을 얻음
        print(v, end=' ')
        nbr = graph[v] - visited
        for u in nbr:
            visited.add(u)
            que.put(u)



# 팩토리얼 (4.1)
def factorial_recur(n):
    if n == 1:
        return 1
    else:
        return factorial_recur(n-1)*n



# 팩토리얼 (4.2)
def factorial_iter(n):
    result = 1
    for k in (1, n+1):
        result = result*k
    return result


# 거듭제곱 (4.4)
"""
x의 n거듭제곱인 x^n을 계산하라
"""
# 억지기법 (반복구조)
def slow_power(x, n):
    result = 1.0
    for i in range(n):
        result = result*x
    return result
# 축소 정복 기법
def power(x, n):
    if n == 0:
        return 1
    elif n%2 == 0:
        return power(x*x, n//2)
    else:
        return x*power(x*x, (n-1)//2)


# 행렬의 거듭제곱 (4.9)
"""
m x m 의 정방렬 행렬 M의 n거듭제곱 M^n을 구하라
"""

def powerMat(x, n):
    if n==1 :
        return x
    elif (n%2)==0:
        return powerMat((multMat(x,x)), n//2)
    else:
        return powerMat(x, powerMat(multMat(x,x), (n-1)//2))
def multMat(M1, M2):
    n = len(M1)
    M3 = list()
    for i in range(n):
        for j in range(n):
            M3[i][j] = 0
            for k in range(n):
                M3[i][j] += M1[i][k]*M2[k][j]
    return M3


# k번째 작은 수 찾기 (4.10)
"""
리스트에서 k번째로 작은 항목을 찾아라. 단, 리스트는 정렬되어있지 않다.
1. 정렬 이용
리스트를 sort() 후에 찾는다
2. 축소 정복
(1) 리스트의 한 항목을 피벗으로 선택한다. 
(2) 리스트의 나머지 항목들을 모두 검사하여 피벅보다 작으면 왼쪽으로 옮기고
피벗보다 크면 오른쪽으로 옮긴다.
"""
# 정렬 이용
def kth_smallest_sort(A, k):
    A.sort()
    return A[k-1]
# 축소 정복 기법 이용
def partition(A, left, right):
    low = left +1
    high = right
    pivot = A[left] # 피벗을 리스트의 맨 왼쪽 항목으로 설정
    while(low<=high): # low와 high가 역전되지 않는 한 반복
        while low <= right and A[low]<pivot: low +=1
        while high >= left and A[high]>pivot: high -=1

        if low < high: # A[low]가 피벗보다 크고 A[high]가 피벗보다 작은 상태
            A[low], A[high] = A[high], A[low]
    A[left], A[high] = A[high], A[low]
    return high
def quick_select(A, left, right, k):
    pos = partition(A, left, right)
    if(pos+1 == left+k):
        return A[pos]
    elif(pos+1 > left+k):
        return quick_select(A, left, pos-1, k)
    else:
        return quick_select(A, pos+1, right, k-(pos+1-left))


# 7장 동적 계획법
"""
- 분할 정복 기법과 비슷하지만, 동적 프로그래밍은 부분 문제들의 답을 어딘가에 저장해 놓고 필요할 때 다시 꺼내서
사용하는 것인데 같은 부분 문제를 다시 풀지 않도록 하는 것이 핵심 아이디어다.
- 한번 푼 문제를 다음에 다시 풀어야 할 때는 그 문제에 대한 저장된 해답을 이용하는 것이 동적 계획법의 기본 아이디어이다.
- 부분 해를 저장하는 2가지 방법은 '메모이제이션'과 '테이블화'이다
1. 메모이제이션
2. 테이블화
결과를 저장할 테이블을 먼저 만든다. 다음으로 답이 이미 알려진 단순한 상황, 
즉 기반 상황에 대한 테이블을 먼저 채우고 이들을 바탕으로 테이블을 채워서 올라간다.
"""

# 피보나치 수열 (7.1)
# 메모이제이션
"""
def fib_dp_mem(n):
    if(mem[n]==None): #풀리지 않은 경우
        if n<2: #기반상황
            mem[n] = n 
        else: #일반상황
            mem[n] = fib_dp_mem(n-1)+fib_dp_mem(n-2)
    return mem[n]
"""
#테이블화
def fib_dp_tab(n):
    f = [None]*(n+1) # n+1크기의 테이블믄 제작
    f[0] = 0 # 기반상황
    f[1] = 1
    for i in range(2, n+1): # 일반상황
        f[i] = f[i-1] + f[i-2]
    return f[n]

#이항계수 (7.3)
#분할 정복 기법
def bino_coef_dc(n, k):
    if k==0 or k==n:
        return 1
    return bino_coef_dc(n-1, k-1) + bino_coef_dc(n-1, k)
#동적 계획법
def bino_coef_dp(n,k):
    C = [[-1 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j==0 or j==i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[n][k]


# 배낭 채우기  (7.5)
# 분할 정복 기법
def knapSack_bf(W, wt, val, n): # W: 현재 배낭의 용량, wt: 물건들의 무게를 저장한 리스트, val: 물건들의 가치를 저장한 리스트, n: 물건들의 수
    if n == 0 or W == 0 : # 기반 상황
        return 0
    if (wt[n-1]>W): # n번째 항목이 배낭 용량보다 크다면
        return knapSack_bf(W, wt, val, n-1) # 넣을 수 없다
    else: # n번째 항목이 배낭 용량보다 작다면
        valWithout = knapSack_bf(W, wt, val, n-1) #이 항목을 넣지 않는 경우와
        valWith = val[n-1] + knapSack_bf(W-wt[n-1], wt, val, n-1) #넣는 경우의 가치를 계산하여 큰 값을 선택해 반환한다
        return max(valWith, valWithout)
# 동적 계산법
def knapSack_dp(W, wt, val, n):
    A = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1]>w: #i번째 물건이 배낭 용량을 초과
                A[i][w] = A[i-1][w]
            else: #i번째 물건이 배낭 용량 이하
                valWith = val[i-1] + A[i-1][w-wt[i-1]]
                valWithout = A[i-1][w]
                A[i][w] = max(valWith, valWithout)
    return A[n][w]





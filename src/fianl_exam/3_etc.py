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
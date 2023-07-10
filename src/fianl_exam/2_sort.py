
# 선택 정렬 [3.1]
"""
1. 선택 정렬
- 입력 리스트에서 가장 작은 항목을 찾고, 이것을 꺼내 정렬된 리스트에 순서대로 저장한다.
2. 제자리 정렬로 개선된 선택 정렬
- 정렬이 안된 리스트에서 최솟값이 선택되면 이 값을 새로운 리스트에 저장하는 것이 아니라 첫 번째 요소와 교환한다.
"""
def selection_sort(A) :
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if(A[j]<A[least]):
                least = j
        A[i], A[least] = A[least], A[j]


# 삽입 정렬 [4.1 축소 정복 기법]
"""
A[0] 이미 정렬되어 있음
A[0] <- A[1]을 정렬된 리스트에 맞는 위치에 삽입
A[0]A[1] <- A[2] 를 정렬된 리스트에 맞는 위치에 삽입
A[0]A[1]A[2] <- A[3] 를 정렬된 리스트에 맞는 위치에 삽입
"""
def insertion_sort(A) :
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key:
            A[j+1] = A[j] # 항목들을 오른쪽으로 한 칸씩 이동
            j = j-1
        A[j+1] = key # 항목 A[i]를 제 위치에 삽입



# 위상 정렬 [4.4 축소 정복 기법]
"""
위상 정렬은 방향 그래프와 관련되어 있다. 방향 그래프는 간선에 방향성이 있는 그래프를 말한다.
방향 그래프 G = (V,E)가 주어졌다. G에 존재하는 각 정점들의 선행 순서를 위배하지 않으면서
모든 정점들을 순서대로 나열하라.
mygraph = { "A" : {"C","D"}, "B" : {"D","E"}, "C" : {"D","F}, D : {"F"}, "E" : {"F"}, "F" : {} }
"""
def topological_sort(graph):
    inDeg = {} # { "정점" : "진입차수" } 저장을 위한 공백 딕셔너리
    for v  in graph: # 그래프의 모든 정점에 대해
        inDeg[v] = 0  # { "정점" : 0 } 으로 초기화
    for v in graph:
        for u in graph[v]: # v와 인접한 모든 정점 u에 대해
            inDeg[u] += 1 # 진입차수 1증가

    vlist = [] # 진입차수가 0인 정점리스트를 만듦
    for v in graph:
        if inDeg[v] == 0: # 진입차수가 0이면 방문 리스트에 추가
            vlist.append(v)

    while vlist:
        v = vlist.pop()
        print(v, end=' ')

        for u in graph[v]: # 연결된 정점의 진입차수 감소
            inDeg[u] -= 1 # 진입차수 감소
            if inDeg[u] == 0:
                vlist.append(u)


# 이진 탐색 [4.5]
"""
리스트의 중앙에 있는 항목들을 먼저 조사한다.
만약 이 항목이 탐색키보다 크다면 찾는 항목은 이 항목 왼쪽에 있고, 
이 항목이 탐색키보다 작다면 찾는 항목은 이 항목의 오른쪽에 있을 것이다. 
"""
# 순환구조
def bianry_search(A, key, low, high): # A: 리스트 key: 찾는 값 low, high: 탐색범위
    if low <= high:
        mid = low+high//2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return bianry_search(A, key, low, mid-1)
        else:
            return bianry_search(A, key, mid+1, high)
    return -1
# 반복구조
def binary_search(A, key, low, high):
    while low<= high:
        mid = (low+high)//2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid-1
        else:
            low = mid+1
    return -1


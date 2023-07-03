"""
위상 정렬(축소 정복 기법)
모든 정점들의 진입차수를 구해서 진입차수가 0인 정점들을 리스트에 저장한다.
리스트가 공백이 아닐때까지 진입차수인 0인 정점을 삭제하면서 해당 정점과 연결된 정점들의 진입차수도 감소시키는 알고리즘이다.


시간복잡도
정점의수를 n 간선의 갯수를 e라고 할때
시간복잡도는 O(n+e)이다.
"""

import time
start=time.time()
# 1번을 해보세요!
def topological_sort(graph):
    inDeg = dict() # 정점 : 진입차수 저장을 위한 딕셔너리
    for i in graph: # 정점 0으로 초기화
        inDeg[i] = 0
    for i in graph: # 모든 정점
        for j in graph[i]: # i에 인접한 모든 정점 j
            inDeg[j] += 1 # 차수 1씩 증가

    visited = [] # 진입차수가 0인 리스트
    for i in graph:
        if inDeg[i] == 0:
            visited.append(i) # 진입차수가 0이면 0인리스트에 추가해

    while visited: # 리스트가 엠프티가 아닐때 까지 반복하는 while문
        i = visited.pop()
        print(i, end=' ')
        for j in graph[i]:
            inDeg[j] -= 1 # 진입차수 1씩 줄임
            if inDeg[j] == 0:
                visited.append(j) # 진입차수가 0이면 0인리스트에 추가


# 2번을 해보세요!
num = int(input()) # 정점의 갯수
line = int(input()) # 간선의 갯수
mygraph = dict() #빈 딕셔너리 생성

for i in range(num):
    mygraph[chr(65+i)] = set() # 정점의 갯수를 입력받고, Key값에 A부터 알파벳 순서로 이루어지게 파이썬의 아스키코드chr() 메소드를 이용한다

for i in range(line):
    dicArr = input().split(' ') #딕셔너리의 Key값과 Value값을 나누기 위한 입력받을 리스트 생성
    mygraph[dicArr[0]].add(dicArr[1]) #간선으로 연결된 두 정점을 딕셔너리에 추가


# 출력합니다!
print('topological_sort: ')
topological_sort(mygraph)
print()
print("실행시간:",time.time()-start)




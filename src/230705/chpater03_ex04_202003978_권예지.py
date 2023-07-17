# 필요한 모듈을 추가해 보세요!
import queue, time
start=time.time()
# 1번을 해보세요!
def bfs(graph, start):
    visited = {start} # 첫 시작은 start만 방문했음
    que = queue.Queue() # 파이썬 큐 모듈의 큐 객체를 생성
    que.put(start) # 선입선출인 큐에 start 정점을 삽입
    while not que.empty(): # 큐가 항목이 하나도 없을 때 반복을 멈춘다
        v = que.get() # 맨 앞에 있는 객체를 큐에서 빼낸다
        print(v, end= ' ') # 방문한 정점 출력
        nbr = graph[v]-visited # v의 인접 정점에서 방문한 정점을 제외한 것을 nbr에 담음
        for u in nbr:
            visited.add(u) # u가 방문했다는 것을 visited에 추가
            que.put(u) # u를 큐에 삽입할 차례이다
    return None


# 2번을 해보세요!
num = int(input()) #횟수 입력받음
mygraph = dict() #빈 딕셔너리 생성

for i in range(num):
    dicArr = input().split(' ') #딕셔너리의 Key값과 Value값을 나누기 위한 입력받을 리스트 생성

    if dicArr[0] or dicArr[1] not in mygraph: # 원소 0,1의 키값이 마이그래프에 없는 경우
        if dicArr[0] not in mygraph: # 원소0의 키값이 마이그래프에 없는 경우
            mygraph[dicArr[0]]=set([dicArr[1]])
        if dicArr[0] in mygraph: # 원소0의 키값이 마이그래프에 있는 경우
            mygraph[dicArr[0]].add(dicArr[1])
        if dicArr[1] not in mygraph: # 원소1의 키값이 마이그래프에 없는경우
            mygraph[dicArr[1]]=set([dicArr[0]])
        if dicArr[1] in mygraph: # 원소1의 키값이 마이그래프에 있는 경우
            mygraph[dicArr[1]].add(dicArr[0])
    else: # 원소 0,1의 키값이 마이그래프에 있는 경우
        mygraph[dicArr[0]].add(dicArr[1])
        mygraph[dicArr[1]].add(dicArr[0])

# 출력합니다!
print('BFS : ', end='')
bfs(mygraph, "A")
print()
print("실행시간:",time.time()-start)

"""
리스트로 표현된 너비 우선 탐색의 시간 복잡도는 O(n+e)
행렬로 표현된 그래프에선 너비 우선 탐색 시간 복잡도는 O(n^2)
"""
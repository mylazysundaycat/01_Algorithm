import time
start=time.time()
# 1번을 해보세요!
def dfs(graph, start, visited ): # 탐색할 graph, 현재 정점 start, 이미 방문한 집합 visited를 매개변수로 받는다
    if start not in visited: # visited(이미 방문한 집함)에 start(현재 정점) 포함되는지 아닌지 조건문 검사
        visited.add(start) # visited에 start가 없다면 추가해준다.
        print(start,end=' ') # 방문한 노드를 출력
        arr = graph[start]-visited # 딕셔너리 graph에 start key값을 통해서 찾고, visited 집합이 가진 원소만큼 제외해준다
        for v in arr: # 재귀함수를 통해 arr의 모든 원소들을 실행시켜준다
            dfs(graph, v, visited)


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
print('DFS : ', end='')
dfs(mygraph, "A", set() )
print()
print("실행시간:",time.time()-start)

"""
시간 복잡도는 그래프가 인접 리스트로 표현 되어있는 경우엔 정점의 수가 n, 간선의 수가 e인 경우 O(n+e)이다
만약 인접 행렬로 표현 되어있다면 어떤 정점이 인접 점정을 찾기 위해선 항상 n번의 비교가 필요할 것이므로
O(n^2)의 시간복잡도로 표현될 것이다
"""
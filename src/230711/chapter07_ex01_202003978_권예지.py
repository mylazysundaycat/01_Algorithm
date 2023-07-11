"""
1. 배낭 채우기 알고리즘
(1) 기반상황
배낭에 넣을 물건이 없다면 n = 0 , val = 0
배낭의 용량이 0이라면 w = 0, val = 0
(2) 일반상황
case1: k번째 물건의 무게가 현재 배낭보다 클 때 -> 배낭에 넣을 수 없고 물건 하나를 뺴준다
case2: k번째 물건의 무게가 현재 배낭보다 작을 때 -> 배낭에 넣는 경우와 넣지 않는 경우를 찾고 이들 중에서 더 큰값을 선택함

2. 시간복잡도
이중 루프를 사용하므로, O(nW) : 외부루프(n) 내부루프(W)
"""

import time
start = time.time()
# 1번을 해보세요!
# 분할 정복 기법
def knapSack_dc(W, wt, val, n):
    if n == 0 or W == 0:  # 기반상황, 물건이 없거나 배낭 용량이 0 이면 최대 가치는 0이다
        return 0

    if wt[n - 1] > W:  # 해당 물건의 무게가 배낭 무게보다 큼
        return knapSack_dc(W, wt, val, n - 1)  # 해당 물건 삭제

    else:  # 해당 물건의 무게가 배낭 무게보다 무겁지 않다면
        valWithout = knapSack_dc(W, wt, val, n - 1)  # 넣지 않는경우
        valWith = val[n - 1] + knapSack_dc(W - wt[n - 1], wt, val, n - 1)  # 넣는 경우
        return max(valWith, valWithout)  # 둘 중에서 큰 값을 리턴함

# 동적 계획법
def knapSack_dp(W, wt, val, n):
    A = [[0 for x in range(W + 1)] for x in range(n + 1)]  # 초깃값이 0인 (n+1)X(W+1) 테이블 생성
    # 물건의 수가 행, 배낭의 용량이 열이다.

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] > w: # i번째 물건이 배낭 용량을 초과시
                A[i][w] = A[i-1][w] # i번째 물건부터의 최대가치는 전에 구해놓은 값을 사용한다
            else : # i번째 물건이 배낭 용량 이하
                valWith = val[i-1] + A[i-1][w-wt[i-1]] # 넣는 경우의 가치
                valWithout = A[i-1][w] # 뺴는 경우의 가치
                A[i][w] = max(valWith, valWithout)

    return A[n][W]
# 2번을 해보세요!
n = int(input())
val = list(map(int, input().split()))
wt = list(map(int, input().split()))
W = int(input())

# 출력합니다!
print("최대 가치_분할 정복 기법:", knapSack_dc(W, wt, val, n))
print("최대 가치_동적 계획법:", knapSack_dp(W, wt, val, n))
print("실행시간:", time.time()-start)
"""
1. 최장 공통 부분순서 LCS
길이가 각각 m과 n인 두 문자열을 비교하는 상황
(1) 기반상황
n, m이 0이라면 두 문자열 중 하나의 길이가 0이다. 따라서 LCS의 길이도 0이다
(2) 일반상황
두 문자열의 맨 뒤쪽 문자부터 먼저 처리한다. 즉 X와 Y의 맨 뒤 문자부터 처리하는데,
이들이 같은 경우와 다른 경우로 분리하여 각각 계산한다. 최종 LCS는 이들 중 더 긴쪽이 된다.

2. 시간 복잡도
O(n^2)
"""

import time
start = time.time()

# 동적 계획법으로 최장 공통 부분순서를 구하는 함수
def lcs_dp(X, Y): # 두개의 문자열 X,Y
    m = len(X)
    n = len(Y)
    L = [[None] * (n + 1) for _ in range(m + 1)] # 초깃값이 None인 (m+1)X(n+1)크기의 테이블 생성

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0: # 기반 상황: 둘 중에 하나라도 길이가 0 일때
                L[i][j] = 0 # LCS는 0이다
            elif X[i - 1] == Y[j - 1]: # 일반 상황1: 마지막 글자가 같으면
                L[i][j] = L[i - 1][j - 1] + 1
            else: # 일반 상황2: 마지막 글자가 다르면
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # 함수 lcs_dp_traceback(X, Y, L)를 호출해요!
    print("LCS = ", lcs_dp_traceback(X, Y, L))
    return L[m][n]


# 1번을 해보세요!
def lcs_dp_traceback(X, Y, L):
    lcs = "" # 출력할 문자열
    i = len(X)
    j = len(Y)
    while i > 0 and j > 0: # 문자열 길이가 둘 다 0이 아닌 동안에 반복
        v = L[i][j] # LCS 테이블을 추적할 변수
        if v > L[i][j - 1] and v > L[i - 1][j] and v > L[i - 1][j - 1]: # 왼쪽, 위쪽, 왼쪽 대각선 위보다 v값이 클 때
            i -= 1
            j -= 1
            lcs = X[i] + lcs # 문자열의 해당 값이 공통부분
        elif v == L[i][j - 1] and v > L[i - 1][j]: # 왼쪽과 값이 같고 위쪽보다 값이 클 때
            j -= 1 # 왼쪽으로 이동
        else: # 그 외의 경우
            i -= 1
    return lcs


# 2번을 해보세요!
X = input()
Y = input()

# 출력합니다!
print("X = ", X)
print("Y = ", Y)
lcs_dp(X, Y)
print("실행시간:", time.time()-start)
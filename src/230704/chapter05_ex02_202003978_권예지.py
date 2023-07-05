"""
1. 코드설명
- 억지기법
행렬의 곱셈의 정의에 따라서 코드를 제작한다
- 쉬트라쎈 알고리즘
분할정복기법을 이용하여 행렬을 4개의 부분 행렬로 분할한다. n은 2의 거듭제곱으로 제한해야 한다.
nxn의 행렬을 2x2행렬로 분해하고 이를 C11,C12,C21,C22로 원소를 정의한다.
이때 내부의 연산을 M1~M7 총 7개로 나누고 이를 C1~C4에 활용한다.

2. 시간복잡도
- 억지기법
O(n^3)
반복문이 3중첩이 되므로 n의 3승이 알고리즘의 복잡도가 된다.
- 쉬트라쎈
O(n^2.81)
그렇지만 n이 2의 거듭제곱이 아니라면 약간의 수정이 필요할 것이다.
"""
import time
import numpy as np
start = time.time()

# 1번을 해보세요!
# 억지 기법
def multiply(A, B, C) :
    for i in range(len(A)):
        for j in range(len(A)):
            C[i][j] = 0
            for k in range(len(A)): #행렬의 곱셈과정
                C[i][j] += A[i][k]*B[k][j]
# 쉬트라쎈 알고리즘
def strassen(A, B):
    n = len(A)
    if n==1: # 1*1행
        return A*B

    n2 = n//2
    A11, A12, A21, A22 = A[:n2, :n2], A[:n2, n2:], A[n2:, :n2], A[n2:, n2:] # 행렬을 2x2로 나누는 과정
    B11, B12, B21, B22 = B[:n2, :n2], B[:n2, n2:], B[n2:, :n2], B[n2:, n2:] # 행렬을 2x2로 나누는 과정

    M1 = strassen(A11+A22, B11+B22)
    M2 = strassen(A21+A22, B11)
    M3 = strassen(A11, B12-B22)
    M4 = strassen(A22, B21-B11)
    M5 = strassen(A11+A12, B22)
    M6 = strassen(A21-A11, B11+B12)
    M7 = strassen(A12-A22, B21+B22)

    C11 = M1+M4-M5+M7
    C12 = M3+M5
    C21 = M2+M4
    C22 = M1+M3-M2+M6

    C = np.vstack((np.hstack((C11,C12)), np.hstack((C21,C22))))

    return C


# 2번을 해보세요!
num = int(input())
A = []
B = []

for i in range(num): # 행렬 A를 받는 반복문
    A.append(list(map(int, input().split())))
for i in range(num): # 행렬 B를 받는 반복문
    B.append(list(map(int, input().split())))
A = np.array(A)
B = np.array(B)

C = []
for i in range(num): # 행렬 C에 0을 채우는 반복문
    C.append([0]*num)


# 출력합니다!

print("억지 기법")
multiply(A, B, C)
print(C)

print("쉬트라쎈 알고리즘")
D = strassen(A,B)
print(D)

print('실행시간:',time.time()-start)
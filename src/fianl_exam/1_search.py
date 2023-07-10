
# 순차 탐색 [3.2]
"""
1. 순차 탐색 (=선형 탐색)
- 입력 리스트의 첫 항목부터 순서대로 하나씩 탐색키와 비교한다
- 하나씩 검사하다가 발견하면 해당 항목의 인덱스를 반환하고, 발견하지 못하면 -1을 반환한다
"""
def sequential_search(A, key): # A는 리스트 Key는 찾고자 하는 값
    n = len(A)
    for i in range(n):
        if A[i]==key:
            return i
    return -1
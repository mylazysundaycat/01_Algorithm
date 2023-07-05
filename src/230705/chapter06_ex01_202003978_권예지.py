
"""
1. 기수정렬

2. 시간복잡도
"""

# 파이썬 queue모듈의 Queue 를 사용해요!
from queue import Queue


# 1번을 해보세요!
def radix_sort(A) :
    queues = []
    for i in range(BUCKETS):
        queues.append(Queue())

    n = len(A)
    factor = 1
    for d in range(DIGITS):
        for i in range(n):
            queues[(A[i]//factor)%10].put(A[i])
        j = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[j] = queues[b].get()
                j += 1
        factor *= 10
        print("step", d+1, A)


# 2번을 해보세요!
data = []


# 출력합니다!
BUCKETS = 10		# 10진법으로 정렬
DIGITS  = 4		# 최대 4 자릿수
radix_sort(data)						# 기수 정렬
print("Radix:", data)					# 결과 출력
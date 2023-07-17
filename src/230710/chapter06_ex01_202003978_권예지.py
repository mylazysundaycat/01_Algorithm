
"""
1. 기수정렬
 시간 효율성을 위해 공간 효율성을 희생한 알고리즘이다. 버킷을들 미리 만들고 정렬되지 않은 항목들을
 일의 자릿수, 십의 자릿수, 백의 자릿수 등에 맞게 정렬해서 담는다. 이때 선입선출을 하는 큐를
 이용하여 정렬한다.
2. 시간복잡도
외부루프 d번(숫자가 d자릿수를 가질때)
O(d*n)
"""

import time
start = time.time()
# 파이썬 queue모듈의 Queue 를 사용해요!
from queue import Queue


# 1번을 해보세요!
def radix_sort(A) :
    queues = [] #큐를 담을 배열
    for i in range(BUCKETS):
        queues.append(Queue())

    n = len(A) #리스트의 크기
    factor = 1 #1번째 자리수 부터 진행

    for d in range(DIGITS): #모든 자릿수를 검사하는 반복문
        for i in range(n):
            queues[(A[i]//factor)%10].put(A[i]) # 자릿수에 맞는 버킷에 담기
        j = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[j] = queues[b].get()
                j += 1
        factor *= 10
        print("step", d+1, A)


# 2번을 해보세요!
data = list(map(int, input().split()))

# 출력합니다!
BUCKETS = 10		# 10진법으로 정렬
DIGITS  = 4		# 최대 4 자릿수
radix_sort(data)						# 기수 정렬
print("Radix:", data)					# 결과 출력
print('실행시간:',time.time()-start)
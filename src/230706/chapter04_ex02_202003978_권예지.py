"""
이진탐색 순환구조와 반복구조의 알고리즘의 틀은 동일하다.
그러나 키값이 mid값보다 작아서 왼쪽 리스트를 탐색할 때
순환구조는 재귀 함수를 통해 오른쪽 인덱스를 변형해서 재귀함수를 호출하지만
반복구조는 조건문을 통해 제어하며 반복구조로 하나의 함수내에서 처리한다.

시간복잡도
log2(N)
"""

import time
start=time.time()

# 1번을 해보세요
#순환구조(재귀함수)
def binary_search(A, key, low, high) :
    if(low<high): #탐색범위 안에 항목들이 남아있다면
        mid=(low+high)//2
        if key == A[mid]: # 키값과 리스트 안의 인덱스의 값이 같다면
            return mid #중간값이 바로 키값이라면
        elif key < A[mid]:
            return binary_search(A, key, low, mid-1) # 키값이 해당 인덱스 값보다 작아서 왼쪽리스트 탐색
        else:
            return binary_search(A, key, mid+1, high) # 키값이 해당 인덱스 값보다 커서 오른쪽 리스트 탐색
    return -1

#반복문
def binary_search_iter(A, key, low, high) :
    while(low<=high): #탐색범위 안에 항목이 남아있다면
        mid = (low+high)//2
        if key == A[mid]:
            return mid #탐색 성공! 중간값이 키값일때
        elif key>A[mid]: #키값이 mid값보다 커서 오른쪽에 있을때
            low = mid+1
        else: #키값이 mid값보다 작아서 왼쪽에 있을때
            high = mid-1
    return -1


# 2번을 해보세요!
listA = input().split(' ') #리스트 입력
key = input() #탐색 키 입력

# 출력합니다!
print("입력 리스트 =", listA)
print("%s 탐색(순환) -->" %(key), binary_search(listA, key, 0, len(listA)-1) )

print("입력 리스트 =", listA)
print("%s 탐색(반복) -->" %(key), binary_search_iter(listA, key, 0, len(listA)-1) )

print("실행시간:",time.time()-start)

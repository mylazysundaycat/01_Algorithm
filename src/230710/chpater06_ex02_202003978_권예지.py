"""
1. 호스풀 알고리즘
문자열 매칭의 억지 기법과는 다르게, 패턴을 뒤에서부터 앞으로 검사한다.
만약 첫 번째 비교에서 불일치가 발생했을 때, 이러한 문자가 패턴 안에 없는 문자라면 더 많이 인덱스를 뛰어서 검사할 수있다.
패턴 안에 있는 문자라면 해당 패턴속의 문자에 맞춰서 검사를 진행할 수 있는 알고리즘으로
억지기법보다 효율적인 알고리즘이다.
2. 시간복잡도
m 패턴의 길이
n 텍스트(입력)의 길이
O(mn)
"""
import time
start = time.time()

NO_OF_CHARS = 128

# 1번을 해보세요!
def shift_table(pat):
    m = len(pat) # 패턴의 길이
    tbl = [m]*NO_OF_CHARS # 시프트 테이블
    for i in range(m-1): # 패턴
        tbl[ord(pat[i])] = m-1-i
    return tbl


# 2번을 해보세요!
def search_horspool(T, P):
    m = len(P) #패턴의 길이
    n = len(T) #입력의 길이
    t = shift_table(P)
    i = m-1
    while(i<=n-1): # 패턴과 텍스트의 매칭과정 반복문
        k=0
        while k<= m-1 and P[m-1-k]==T[i-k]:
            k += 1
        if k==m:
            return i-m+1
        else:
            i+=t[ord(T[i])]
    return -1


# 3번을 해보세요!
text = input()
pattern = input()


# 출력합니다!
print("패턴의 위치 :", search_horspool(text, pattern))
print('실행시간:',time.time()-start)
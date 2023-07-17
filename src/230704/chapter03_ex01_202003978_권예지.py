import time
start=time.time()
# 1번을 해보세요!
def string_matching(T, P):
    n = len(T) # 문자열 T의 길이를 n에 저장
    m = len(P) # 문자열 P의 길이를 m에 저장
    for i in range(n-m+1): # 문자열 T와P의 길이의 차이만큼 반복한다
        j = 0
        while j<m and P[j]==T[i+j]: # j가 문자열 P의 길이보다 작고 P의 요소와 T의 요소의 값이 일치할때 반복문이 실행
            j += 1 # 반복문이 실행시에 j의 값이 한개씩 증가한다
            if j == m: # j가 문자열 P의 길이와 값이 같아지면 문자열 T안에 문자열 P를 찾은 것이므로 해당 index값을 리턴한다
                return i
    return -1 # 문자열 T 속에서 문자열 P을 찾지 못하였으므로 -1을 리턴한다

# 2번을 해보세요!
T = input()
P = input()

# 출력합니다!
print(string_matching(T, P))
print("실행시간:",time.time()-start)
# 필요한 모듈을 추가해 보세요!
import math, time
start=time.time()
# 1번을 해보세요!
def closest_pair(p):
    n = len(p) # 리스트 p의 길이
    min = float("inf") # 무한대의 실수 표현
    for i in range(n-1): # 리스트 p내의 두 개의 튜플을 비교해야 하기 때문에 p의 길이보다 1개 적게 반복한다.
        for j in range(i+1, n): # i번째 인덱스와 비교해야 하기 때문에 i+1번째부터 n번째까지로 범위를 조정한다.
            dist = math.sqrt((p[i][0]-p[j][0])**2+(p[i][1]-p[j][1])**2) # 제곱근을 이용하여 유클리드 거리계산
            if dist < min: # 최소값을 찾기 위해 min보다 작은 거리를 mindist에 저장
                min = dist
    return min


# 2번을 해보세요!
num = int(input()) # 리스트의 요소 갯수 입력
p = [] # p=[(1,2),(3,4),(10,35)...] 좌표를 추가해줄 리스트 생성
for i in range(num):
    s = input().split(" ") # '3 4' 이런식으로 입력받을 숫자를 스페이스바 기준으로 나눠서 s에 리스트로 저장
    p.append((int(s[0]),int(s[1]))) # (3,4) 튜플 형식으로 저장할 수 있도록 s의 0번째 요소와 1번째 요소를 쪼개서 저장


# 출력합니다!
print("최근접 거리:", closest_pair(p))
print("실행시간:",time.time()-start)
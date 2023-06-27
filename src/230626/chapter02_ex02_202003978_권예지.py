# chapter02_ex02_202003978_권예지
"""
하노이의 탑
재귀적으로 쪼개보면 3가지 경우가 나온다.
1. 원판 n 위에 있는 원판들을 temp에 옮긴다
2. 가장 밑에있는 원판n을 to로 옮긴다
3. temp에 있는 원판들을 to로 옮긴다
"""
def hanoi_tower(n, fr, temp, to):
    if n==1: #재귀함수의 종료지점. 원판이 1개일 경우 이동시키는 것을 의미하고 하노이의 탑 재귀 과정에서 1번에 해당된다.
        print("원판1 : %s -> %s" %(fr,to))
    else:
        hanoi_tower(n-1, fr, to, temp) #밑에있는 원판들을 temp로 옮기는 과정
        print("원판%d : %s -> %s" %(n,fr,to))
        hanoi_tower(n-1,temp, fr, to) #temp에 옮겨진 원판들을 to로 옮기는 과정

"""
원판 N개
A1 = 1
A2 = 2*A1 + 1
A3 = 2*A2 + 1
.
.
.
AN = 2*An-1 + 1 번
따라서 시간복잡도는 2^N 이다
"""

hanoi_tower(4,'A','B','C')
print("시간 복잡도는 O(2^N)")

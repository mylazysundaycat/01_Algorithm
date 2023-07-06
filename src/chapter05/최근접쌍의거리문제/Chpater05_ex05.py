#20230706

import math

#띠 영역에서 d보다 작은 최근접 쌍의 거리 찾기
def strip_closet(P, d): #띠 영역의 점 리스트 P
    n = len(P) #띠 영역의 점 갯수
    d_min = d
    P.sort(key = lambda point: point[1]) #y를 기준으로 정렬한다
    """
    익명함수 lambda, point[1] 기준으로 sort()함수를 사용하겠다는 뜻이다.
    즉, 리스트 안의 튜플의 두번째 값인 y를 기준으로 정렬한다
    lambda 인자 : 식
    """
    for i in range(n):
        j = i+1
        while j<n and (P[j][1]-P[i][1])<d_min:
            dij = dist(P[i], P[j])
            if dij < d_min:
                d_min = dij
            j += 1
        return d_min

#두 점의 거리
def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

#최근접 쌍의 거리
def closest_pair_dist(P, n):
    if n <= 3:
        return "억지기법 알고리즘(3.4절)"

    mid = n//2 #중앙점을 찾는다
    mid_x = P[mid][0]

    dl = closest_pair_dist(P[:mid], mid)
    dr = closest_pair_dist(P[mid:], n-mid)
    d = min(dl, dr) #둘중에서 짧은거리

    #중앙에서 x좌표가 d이내인 점들의 집합Pm을 만듬
    Pm = []

    #중앙의 띠 영역의 점들을 리스트로 만드는 과정
    for i in range(n):
        if abs(P[i][0] - mid_x) < d:
            Pm.append(P[i])

    #띠 영역에서 최근접 쌍의 거리를 구한다
    ds = strip_closet(Pm, d)
    return min(d, ds)




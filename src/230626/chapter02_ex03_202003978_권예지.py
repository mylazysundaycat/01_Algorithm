# chapter02_ex03_202003978_권예지
import time
start=time.time()
def binary_digits(n):
    #recursion을 종료할 수 있게 만들어주는 조건식
    if(n//2==0): #n을 나누었을때 몫이 0이면, 나머지가 반환되며 반복이 종료되어야 한다.
        return n%2
    #recursion이 발생하는 라인
    else:
        b = n%2 #입력한 값의 나머지를 담아줄 변수
        n = n//2 #재귀가 될 때 몫이 담긴 변수가 매개변수가 되도록 변경해주는 라인
        return str(binary_digits(n))+str(b)
        """
        첫 번째 시도, 단순히 return binary_digits(n)+b 를 해주었다가 '3'이 출력됨
        두 번째 시도, str(b)+str(binary_digits(n)) 으로 재귀함수 콜 했다가 13을 입력했을때 이진수 1011로 출력됨(1101이 출력되어야함)
        세 번째 시도, str(b)를 재귀함수 뒤로 바꿔주니 원하는 대로 이진수 비트가 출력됨 성공!
        """
print(binary_digits(13))
print("실행시간:",time.time()-start) #구글링을 통해 time 함수를 찾아 사용했다.
print("시간 복잡도는 O(log2N)") #시간복잡도
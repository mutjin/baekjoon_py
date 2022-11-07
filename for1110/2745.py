"""
문제
B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.

10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

입력
첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)

B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.

출력
첫째 줄에 B진법 수 N을 10진법으로 출력한다.
"""

#solution 1
n,b=input().split()

n=list(n) #숫자
b=int(b) #b진법

nlen=len(n)
sum=0

#big endian이다
for i in range(nlen):
    temp=ord(n[i]) #int값 반환

    #알파벳인경우
    if 65<=temp<=90:
        temp-=55
    
    #숫자인경우
    else:
        temp=int(n[i])

    #각 자리의 숫자들의 합
    sum+=temp*pow(b,nlen-1-i)

print(sum)

"""
#solution 2
n, b = input().split()

#int(변환할string, n진법)
print(int(n,int(b)))
"""
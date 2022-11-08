"""
문제
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

출력
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.
"""

n=int(input())
temp=n
lst=[]

"""
소수의 경우 자기자신이 return된다.
따라서 for i in range(2,n) 이면 틀리다.
"""

for i in range(2,n+1):
    while temp%i==0:
        lst.append(i)
        temp/=i

lenlst=len(lst)
for i in range(lenlst):
    print(lst[i])


"""
문제
자연수 n개가 주어진다. 이 자연수의 공약수를 모두 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. n은 2 또는 3이다. 둘째 줄에는 공약수를 구해야 하는 자연수 n개가 주어진다. 모든 자연수는 108 이하이다.

출력
입력으로 주어진 n개 수의 공약수를 한 줄에 하나씩 증가하는 순서대로 출력한다.
"""

from math import gcd #greast common divisor
from math import sqrt #square root

n=int(input())

"""최대공약수 구하기"""
if n==2:
    a,b=map(int,input().split())
    _gcd=gcd(a,b)
elif n==3:
    a,b,c=map(int,input().split())
    _gcd=gcd(gcd(a,b),c)
else:
    print("wrong input")

"""최대공약수의 약수 구하기"""

"""
for i in range(1,_gcd+1):
    if _gcd%i==0:
        print(i)
"""

half=int(sqrt(_gcd))
lst=[]
for i in range(1,half+1):
    if _gcd%i==0:
        lst.append(i)
        if i**2!=_gcd:
            lst.append(_gcd//i)
lst.sort()

lenlst=len(lst)
for i in range(lenlst):
    print(lst[i])
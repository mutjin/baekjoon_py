"""
문제
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

입력
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

출력
M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 

단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
"""

from math import sqrt #square root

def prime_long(x):
    if x==1:
        return False
    else:
        for i in range(2,x):
            if x%i==0:
                return False
            else:
                continue
        return True #들여쓰기주의

"""
소수의 경우 제곱수를 제외하면 약수가 페어로 존재한다
따라서 약수를 빠르게 구하기 위해서는 제곱근까지만 약수를 구하면 된다
"""

def prime_short(x):
    if x==1:
        return False
    else:
        x=int(sqrt(x))+1
        for i in range(2,x):
            if x%i==0:
                return False
            else:
                continue
        return True #들여쓰기주의

m=int(input())
n=int(input())

my_min=-1
my_sum=0

for i in range(m,n+1):
    if prime_long(i)==True and my_min<0:
        my_min=i
        my_sum+=i
    elif prime_long(i)==True and my_min>0:
        my_sum+=i
    else:
        continue

if my_min==-1:
    print(my_min)
else:
    print(my_sum)
    print(my_min)

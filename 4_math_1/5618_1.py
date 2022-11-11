"""
문제
자연수 n개가 주어진다. 이 자연수의 공약수를 모두 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. n은 2 또는 3이다. 둘째 줄에는 공약수를 구해야 하는 자연수 n개가 주어진다. 모든 자연수는 108 이하이다.

출력
입력으로 주어진 n개 수의 공약수를 한 줄에 하나씩 증가하는 순서대로 출력한다.
"""
n=int(input())
lst=[]

if n==2:
    a,b=map(int,input().split())
    smallest=min(a,b)
    for i in range(1,smallest+1):
        if a%i==0 and b%i==0:
            lst.append(i)

elif n==3:
    a,b,c=map(int,input().split())
    smallest=min(a,b,c)
    for i in range(1,smallest+1):
        if a%i==0 and b%i==0 and c%i==0:
            lst.append(i)

else:
    print("wrong input")

lenlst=len(lst)
for i in range(lenlst):
    print(lst[i])

"""
시간 초과 발생했다
"""
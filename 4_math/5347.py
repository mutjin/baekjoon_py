"""
문제
두 수 a와 b가 주어졌을 때, a와 b의 최소 공배수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 n이 주어진다. 
다음 n개 줄에는 a와 b가 주어진다. 
a와 b사이에는 공백이 하나 이상 있다. 
두 수는 백만보다 작거나 같은 자연수이다.

출력
각 테스트 케이스에 대해서 입력으로 주어진 두 수의 최소공배수를 출력한다.
"""
from math import lcm #least common magnitude

n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(lcm(a,b))
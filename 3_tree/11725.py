"""
문제
루트 없는 트리가 주어진다. 
이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
"""
import sys

n=int(input())
lst=[[] for i in range(n+1)]

for i in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)

visited=[0 for i in range(n+1)]
def dfs(tarnode):
    for i in lst[tarnode]: #tarnode와 연결된 노드들 중
        if visited[i]==0: #아직 방문되지 않은 노드는 tarnode의 자식노드
            visited[i]=tarnode #부모노드의 위치에 tarnode 기록
            return dfs(i) #자식노드에 대해서도 순환적으로 진행
        else:
            continue

dfs(1)

for i in visited[2:]:
    print(i)


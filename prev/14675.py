def is_cutvertex(k):

def is_bridge(k):

n=int(input())
treelst=[[-1 for i in range(n)] for i in range(n)]

for i in range(n-1):
    a,b=map(int,input().split())
    treelst[a][b]=1
    treelst[b][a]=1

q=int(input())
for i in range(q):
    t,k=map(int,input().split())
    if t==1:
        is_cutvertex(k)
    elif t==2:
        is_bridge(k)
    else:
        continue

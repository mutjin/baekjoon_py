case=0
lst = []
while True:
    temp = list(map(int, input().split()))
    if temp:
        if temp[-1]<0 and temp[-2]<0:
            break
        else:
            lst.extend(temp)
    print(lst)

lenlst=len(lst)
treelst=[[] for i in range(lenlst//2)]
for i in range(0,lenlst-1,2):
    treelst[lst[i]].append(lst[i+1])

print("Case {} is a tree.".case)
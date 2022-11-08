def prime_long(x):
    if x==1:
        return False
    elif x==2:
        return True
    else:
        for i in range(2,x):
            if x%i==0:
                return False
            else:
                continue
        return True #들여쓰기 주의

for i in range(1,100):
    if prime_long(i)==True:
        print(i,end=" ")
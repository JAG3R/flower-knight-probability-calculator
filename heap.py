def factorial(x):
    X=1
    for i in range(x):X*=i+1
    return X
def carry(A,time):
    for _ in range(time):
        X=range(len(A))
        X.reverse()
        if A[-1]==0:
            for x in X:
                if A[x]>0:
                    A[x]-=1
                    A[x+1]+=1
                    break
        else:
            if A[-2]>0:
                A[-2]-=1
                A[-1]+=1
            else:#carry
                for x in X[1:]:
                    if A[x]>0:
                        A[x]-=1
                        A[x+1]+=A[-1]+1
                        A[-1]=0
                        break
    return A

def heap(m,n):
    A,heaps=[n],[]
    A.extend([0 for _ in range(m-1)])
    A=tuple(A)
    H=factorial(n+m-1)/(factorial(n)*factorial(m-1))
    for i in range(H):heaps.append(carry(list(A),i))
    return heaps

###m:groups, n:objects
##m,n=5,3
##test=heap(m,n)
##print test

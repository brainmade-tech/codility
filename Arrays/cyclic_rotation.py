def solution(A,K):
    if len(A) != 0 and A != None:
        for i in range(K):
            A.insert(0,A.pop())
    return A

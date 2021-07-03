from typing import Counter

def solution(A):
    counter = Counter(A)
    A = [key for key in counter if counter[key]%2 == 1]
    return A[0]
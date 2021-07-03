from typing import Counter

def solution(A):
    counter = Counter(A)
    for nb in counter:
        if counter[nb] % 2 == 1:
            return nb
    return -1

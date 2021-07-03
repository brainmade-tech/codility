def solution(A):
    left_sum = A[0]
    right_sum = sum(A) - left_sum
    minimum = abs(left_sum - right_sum)
    for i in range(2,len(A)):
        left_sum += A[i-1]
        right_sum -= A[i-1]
        tmp_min = abs(left_sum - right_sum)
        if minimum > tmp_min:
            minimum = tmp_min
    return minimum

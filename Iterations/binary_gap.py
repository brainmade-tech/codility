def solution(N):
    N2 = bin(N)[2:]
    if ("10" not in N2) and ("01" not in N2):
        return 0
        
    i = 0
    j = 2
    max = 0
    while i < len(N2)-2 and j < len(N2):
        if N2[i:i+2] == "10":
            if N2[j] != "1":
                j += 1
            else:
                if max < j-i-1: # number of zeros between two ones equals : j-i-1
                    max = j-i-1
                i = j
                j += 2
        else:
            i += 1

    return max
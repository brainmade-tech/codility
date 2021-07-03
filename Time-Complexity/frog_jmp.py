def solution(X, Y, D):
    if X > Y or D <= 0:
        return 0
    nb_step = (Y-X)/D
    if nb_step - int(nb_step) == 0:
        return int(nb_step)
    return int(nb_step) + 1

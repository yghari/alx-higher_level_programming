#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_sum = sum(score * weight for score, weight in my_list)
    score = sum(weight for _, weight in my_list)

    return total_sum / score if score != 0 else 0

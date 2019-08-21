def positive_sum(arr):
    answer = 0
    for num in arr:
        if num > 0:
            answer += num
    return answer

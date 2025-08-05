def solution(diffs, times, limit):
    left, right = 0, max(diffs)

    while (left+1<right):
        lv = (left+right)//2
        limit_tmp = limit
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            if diff<=lv:
                limit_tmp -= time_cur
            else:
                time_prev = times[i-1]
                limit_tmp -= ((diff-lv)*(time_cur+time_prev)+time_cur)
        if limit_tmp<0:
            left = lv
        elif limit_tmp>=0:
            right = lv

    answer = right
    return answer

print(solution([1,4,4,2],[6,3,8,2],59))
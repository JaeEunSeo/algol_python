# lv2 의상

def solution(clothes):
    answer = 1
    closet = dict()
    for c in clothes:
        if c[1] not in closet.keys():
            closet[c[1]] = 1
        closet[c[1]] += 1
    
    for v in closet.values():
        answer *= v
                
    return answer-1   
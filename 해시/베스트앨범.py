# lv2 베스트앨범

def solution(genres, plays):
    answer = []
    g_dict = {}

    for g in genres:
        g_dict[g] = [0]
    
    for i in range(len(genres)):
        g_dict[genres[i]][0] += plays[i]
        g_dict[genres[i]].append({i:plays[i]})


    sorted_data = dict(sorted(g_dict.items(), key=lambda item: item[1][0], reverse=True))
    
    
    for s in sorted_data.values():
        s = sorted(s[1:], key=lambda x: list(x.values())[0], reverse=True)
        for i in s[:2]:
            for k in i.keys():
                answer.append(k)
    
    return answer
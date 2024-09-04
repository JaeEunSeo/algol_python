def solution(numbers, target):
    answer = 0
    graph = [[0]]
    while numbers:
        new_g = []
        new_n = numbers.pop(0)
        for node in graph[-1]:
            new_g.extend([node + new_n, node - new_n])
        graph.append(new_g)
    answer = graph[-1].count(target)
    return answer
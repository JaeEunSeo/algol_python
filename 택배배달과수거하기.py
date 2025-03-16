def solution(cap, n, deliveries, pickups):
    answer = 0
    dcap, pcap = 0, 0
    for j in range(n-1, -1, -1):
        if deliveries[j]!=0 or pickups[j]!=0:
            cnt = 0
            while dcap<deliveries[j] or pcap<pickups[j]:
                cnt += 1
                dcap += cap
                pcap += cap
            dcap -= deliveries[j]
            pcap -= pickups[j]
            answer += (j+1)*cnt*2
                
    return answer

print(solution(5, 3, [5, 0, 5], [0, 1, 10]))
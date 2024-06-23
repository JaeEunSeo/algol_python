N = int(input())
values = [0]

for _ in range(N):
    k = int(input())
    values.append(k)

#print(dp)

if N==1:
    print(values[1])
else:
    dp = {'True':[0] * (N+1), 'False':[0] * (N+1)}
    dp['True'][1] = values[1]
    dp['True'][2] = values[2]
    dp['False'][2] = dp['True'][1] + values[2]
    for i in range(3,N+1):
        dp['False'][i] = dp['True'][i-1] + values[i]
        dp['True'][i] = max(dp['False'][i-2] + values[i], dp['True'][i-2] + values[i])

    k = dp['True'][N]
    p = dp['False'][N]
    print(max(k,p))
self_number = []
i = 1

while True:
    num = i
    i_str = str(i)
    for k in i_str:
        num += int(k)
    if i > 10000:
        break
    self_number.append(num)
    i += 1

for k in range(1,10001):
    if k not in self_number:
        print(k)
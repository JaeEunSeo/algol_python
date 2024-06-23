# AC


T = int(input())

def R(ary):
    tmp = ary.copy()
    tmp.reverse()
    return tmp

def D(ary):
    tmp = ary.copy()
    if len(tmp)==0:
        return 'error'
    tmp = tmp[1:]
    return tmp

for _ in range(T):
    p = input()
    n = int(input())
    input_str = input()

    # 대괄호 제거 및 쉼표로 분리
    str_list = input_str.strip('[]').split(',')

   # print("정수 변환: ", str_list)
    # 각 요소를 정수로 변환
    if len(str_list)==0 or '' in str_list:
        ary = []
    else:
        ary = [int(num) for num in str_list]
        
    
    for command in p:
        if command=='R':
            ary = R(ary)
        if command=='D':
            ary = D(ary)
        if ary=='error':
            break
    print(ary)
# 1700
# 키보드, 헤어드라이기, 핸드폰 충전기, 카메라 충전기
N, M = map(int, input().split())
data_list = list(map(int, input().split()))

multitap = [0] * N
# 이미 꽃혀있는경우
# 비어 있는 경우
# 빈 공간이 없는 경우
# 1. 꽂혀 있는 것중 나중에 안쓰는 것 -> 이거 빼면 되
# 2. 꽂혀 있는 것중 나중에 다 쓰는거면 제일 나중에 쓰는걸 빼
res = swap = num = max_l = 0
#[1,2,3,4,1,2,3]
for i in data_list:
    if i in multitap:
        pass
    elif 0 in multitap:
        multitap[multitap.index(0)] = i
    else:
        for j in multitap:
            if j not in data_list[num:]:
                swap = j
                break
            elif data_list[num:].index(j) > max_l:
                max_l = data_list[num:].index(j)
                swap = j
        multitap[multitap.index(swap)] = i
        max_l = swap = 0
        res += 1
    num += 1
print(res)

    




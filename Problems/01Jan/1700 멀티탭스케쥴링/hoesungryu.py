import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stuff = list(map(int, input().split()))

cnt = 0 
plug_on = []

for i in range(K):
    
    # 해당 기기가 플러그 꽂혀있으면 continue
    if stuff[i] in plug_on:
        continue
    
    # 빈곳이 있으면 그냥 꼿음 continue
    if len(plug_on) < N:
        plug_on.append(stuff[i])
        continue
    
    # 빈 곳 없다. ==> 플러그에서 뒤에서 사용하지 않거나, 가장 나중에 사용하는걸 뽑아야한다
    cnt +=1 # 플러그 뽑아야서 +1 
    out= outidx = 0  # 뽑을 플러그와 stuff 에서 idx 
    for j in range(N):
        try:
            # Case1)  꼿혀있는 것이 이후 사용되는 경우 
            idx = stuff[i+1:].index(plug_on[j])
            if idx > outidx:
                out = j
                outidx = idx 
        except:
            # Case2) 사용안되는경우 
            out = j 
            break   
    plug_on[out] = stuff[i] 
    
print(cnt)


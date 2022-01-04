import sys

'''
최초 값인 Test case의 값 저장
sys.stdin.readline().rstrip()를 이용하여 \n 형태의 input을 차례차례 읽어들인다.
'''

num = int(sys.stdin.readline().rstrip())
i = 0

'''
## 정수 k(층 정보)와 n(호 정보)를 각각 list에 저장한다.
'''

floor = []
place = []
while i < num:
    i += 1
    floor.append(int(sys.stdin.readline().rstrip()))
    place.append(int(sys.stdin.readline().rstrip()))

'''
해당 층과 호의 거주민 수를 알기 위해서는 해당 층 밑에 있는 모든 호수의 인원을
알아야 한다.
ex) 3층 3호의 인원을 알기 위해서는 2층 1,2,3호의 값을 알아야 하고,
    2층 인원을 알기 위해서는 1층 1,2,3호의 값을 알아야 한다.

이를 한번에 해결하기 위해, 층과 호의 max값을 출력하여 해당 호수에 있는 모든
인원을 구하는 방식으로 접근하였다.
worst case: k=14, n=14: 모든 아파트를 다 알아야 한다. 
'''
max_floor = max(floor)
max_place = max(place)

'''
Apart에 dictionary 형태로 층과 호수에 대한 정보를 저장하였다.
apart[0]: 0층에 해당하는 호수
apart[1]: 1층에 해당하는 호수
'''
zero_floor = list(range(1,max_place+1))
apart = dict()
apart[0] = zero_floor

for i in range(1, max_floor + 1):
    floor_list = []
    for j in range(1, max_place + 1):
        floor_list.append(sum(apart[i-1][:j]))
    apart[i] = floor_list


'''
예제 케이스
apart[0] = [1,2,3]
apart[1] = [1,3,6]
apart[2] = [1,4,10]

k층 n호: apart[k][n-1]
'''
for n in range(num):
    print(apart[floor[n]][place[n]-1])
    
    
'''
메모리제한: 128MB, 시간제한: 1s
Memory: 29200KB, 시간: 64ms, 코드길이: 563B
'''

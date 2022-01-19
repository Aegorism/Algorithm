import sys
from functools import reduce

for testcase in range(int(sys.stdin.readline())):

    clothes = {}
    for _case in range(int(sys.stdin.readline())):
        
        value, key = sys.stdin.readline().split()
        if clothes.get(key) is None:
            clothes[key] = {value}
        else:
            clothes[key].add(value)

    num_clothes = [len(v) for v in clothes.values()]
    print(reduce(lambda x, y: x*(y+1), [1] + num_clothes) - 1)
            

if __name__=="__main__":

    pass
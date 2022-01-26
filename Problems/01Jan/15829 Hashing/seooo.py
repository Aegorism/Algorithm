length= int(input())
string = str(input())
r = 31
M = 1234567891


answer = 0
for i in range(length):
    num = ord(string[i]) - 96
    answer += num * (r**i)
print(answer % M)
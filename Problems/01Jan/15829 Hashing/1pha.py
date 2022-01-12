def solution(L, string):

    alphabet2num = {chr(c): idx for c, idx in zip(range(ord("a"), ord("z") + 1), range(1, 27))}
    return sum(31**pos * alphabet2num[s] for pos, s in zip(range(L), string)) % 1234567891

if __name__=="__main__":

    test_cases = [
        {"L": 5, "string": "abcde"},
        {"L": 3, "string": "zzz"},
        {"L": 1, "string": "i"}
    ]

    for test_case in test_cases:
        print(solution(**test_case))
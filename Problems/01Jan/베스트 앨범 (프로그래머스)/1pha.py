from itertools import chain
def solution(genres, plays):    
    # 장르 > 플레이수 > 고유번호
    # 장르 별로 2곡씩
    
    organized = {}
    for idx, (g, p) in enumerate(zip(genres, plays)):
        if organized.get(g) is None:
            organized[g] = [[(idx, p)], p]
        else:
            organized[g][0].append((idx, p))
            organized[g][0] = sorted(organized[g][0], key=lambda x: x[1], reverse=True)[:2]

            organized[g][1] += p

    sorted_organized = sorted(organized.values(), key=lambda x: x[1], reverse=True)
    answer = list(chain(*[[j[0] for j in i[0]] for i in sorted_organized]))
    
    return answer

if __name__=="__main__":

    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]

    print(solution(genres, plays))

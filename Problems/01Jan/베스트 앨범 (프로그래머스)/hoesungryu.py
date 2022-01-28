from collections import defaultdict

def solution(genres, plays):
    genres_sum = defaultdict(int)
    music_dic = defaultdict(list)
    answer=[]

    for cnt,(genre,play) in enumerate(zip(genres,plays)):
        genres_sum[genre]+=play
        music_dic[genre].append([cnt, play])
        
    sorted_genres_sum = sorted(genres_sum.items(), key=lambda x: x[1], reverse=True)

    for key, _ in sorted_genres_sum:
        tmp = sorted(music_dic[key], key=lambda x: x[1], reverse=True)
        for index, play in tmp[:2]:
            answer.append(index)
        
    return answer
from collections import defaultdict

'''
N : 빌딩 층수
K : 엘리베이터 디스플레이 자릿수
P : 반전시킬 LED 최대 갯수 ( 1 >=)
X : 현재 엘리베이터 층수

    0
1       2
    3
4       5
    6

'''
dic = {
    '0': '1110111',
    '1': '0010010',
    '2': '1011101',
    '3': '1011011',
    '4': '0111010',
    '5': '1101011',
    '6': '1101111',
    '7': '1010010',
    '8': '1111111',
    '9': '1111011'
}

def currentLevel(K, X):
    return ''.join(['0' for _ in range(K - len(str(X)))])+str(X)

def checker(K, P, origin, target):
    target = currentLevel(K, target)
    count = 0
    # 자릿수
    for i in range(K):
        # num of LED
        for j in range(7):
            if dic[origin[i]][j] != dic[target[i]][j]: 
                count += 1
                if count > P: return False
    return True if count > 0 else False

def solution():
    N, K, P, X = map(int, input().split())
    number = currentLevel(K, X)
    answer = 0
    for i in range(1, N+1):
        if i == X: continue
        if checker(K, P, number, i): answer += 1
    return answer

print(solution())
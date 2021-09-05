import heapq
'''
input

6 11
5 2 8 4 3 5

'''
def check(lineNum, n, x, data):
    hq = []
    # N 개의 공정 만들기
    for i in range(lineNum):
        heapq.heappush(hq, 0)
    # 각 공정중 제일 작은 애 빼서 더하고 다시 넣기
    for i in range(n):
        heapq.heappush(hq, (heapq.heappop(hq) + data[i]))
    # 제일 오래 작업하는 공정이 x 넘어가면 안됨
    while hq:
        top = heapq.heappop(hq)
    return True if top <= x else False

def solution():
    N, X = map(int, input().split())
    presents = list(map(int, input().split()))
    # 서치
    s, e = 1, 10**5
    while s < e :
        x = (s+e) >> 1
        if check(x, N, X, presents): e = x
        else: s = x+1
    return s

print(solution())
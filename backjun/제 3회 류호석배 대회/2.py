import heapq
from collections import defaultdict

'''
7
1 Cpp 5 10 4 2 8 4
1 Java 2 8 2
2 Cpp 2
--- total 18
1 Cpp 2 10 3
2 Cpp 3
--- total 18 + 19 = 37
2 Java 1
--- total 37 + 8 = 45 ? 
2 Python 10
'''
def solution():
    K = int(input())
    total = 0
    queries = [ input().split() for _ in range(K) ]
    gorilas = defaultdict(list)
    for query in queries:
        if query[0] == '1':
            for info in range(3, len(query)):
                heapq.heappush(gorilas[query[1]], -int(query[info]))
        else:
            for _ in range(int(query[2])):
                if len(gorilas[query[1]]) > 0:
                    total += -heapq.heappop(gorilas[query[1]])
                else: break
    return total

print(solution())
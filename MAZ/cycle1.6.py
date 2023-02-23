#all pair shortest path
v = 4
INF = 99999
def floydWarshall(graph):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    printSolution(graph)

def printSolution(graph):
    print("The shortest pair path is:")
    print()
    for i in range(v):
         for j in range(v):
             if (graph[i][j] == INF):
                  print("%7s" % "INF", end=" ")
             else:
                 print("%7d" % (graph[i][j]), end=' ')
                 if j == v-1:
                     print()
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
         ]

floydWarshall(graph)
def check_product(): 
    f = open("test.in", "r")
    expresii = f.read().split("\n")
    output = ""
    for expresie in expresii:
        leftside, p = expresie.split("=")
        p = int(p)
        a, b = leftside.split("*")
        a = int(a)
        b = int(b)
        if a * b == p:
            output += expresie + " Corect\n"
        else:
            output += expresie + " Gresit " + str(a * b) + "\n"
    o = open("test.out", "w")
    o.write(output)

def check_occurences():
    propozitie = input().split();
    d = {x: propozitie.count(x) for x in propozitie}
    minval = len(propozitie) + 1
    maxval = 0
    mincuv = ""
    maxcuv = ""
    for cuvant in d:
        if d[cuvant] > maxval or (d[cuvant] == maxval and cuvant < maxcuv):
            maxval = d[cuvant]
            maxcuv = cuvant
        if d[cuvant] < minval or (d[cuvant] == minval and cuvant < mincuv):
            minval = d[cuvant]
            mincuv = cuvant
    print(mincuv, maxcuv)

#kmp algorithm
def kmp(s, t):
    n = len(s)
    m = len(t)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and t[k] != t[q]:
            k = pi[k - 1]
        if t[k] == t[q]:
            k += 1
        pi[q] = k
    q = 0
    for i in range(n):
        while q > 0 and t[q] != s[i]:
            q = pi[q - 1]
        if t[q] == s[i]:
            q += 1
        if q == m:
            return i - m + 1
    return -1


#max flow algorithm

def bfs(graph, source, sink):
    n = len(graph)
    visited = [False for i in range(n)]
    queue = []
    queue.append(source)
    visited[source] = True
    parent = [-1 for i in range(n)]
    while queue:
        u = queue.pop(0)
        for v in range(n):
            if visited[v] == False and graph[u][v] > 0:
                queue.append(v)
                parent[v] = u
                visited[v] = True
    path = []
    if visited[sink] == True:
        v = sink
        while v != -1:
            path.append(v)
            v = parent[v]
        path.reverse()
    return path

def max_flow():
    n = int(input())
    m = int(input())
    graph = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        a, b, c = input().split()
        a = int(a)
        b = int(b)
        c = int(c)
        graph[a][b] = c
    source = int(input())
    sink = int(input())
    flow = 0
    while True:
        path = bfs(graph, source, sink)
        if path == []:
            break
        mincap = 1000000000
        for i in range(len(path) - 1):
            mincap = min(mincap, graph[path[i]][path[i + 1]])
        for i in range(len(path) - 1):
            graph[path[i]][path[i + 1]] -= mincap
            graph[path[i + 1]][path[i]] += mincap
        flow += mincap
    print(flow)


#min cost max flow algorithm

def min_cost_max_flow():
    n = int(input())
    m = int(input())
    graph = [[0 for i in range(n)] for j in range(n)]
    cost = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        a, b, c, d = input().split()
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        graph[a][b] = c
        cost[a][b] = d
    source = int(input())
    sink = int(input())
    flow = 0
    costflow = 0
    while True:
        path = bfs(graph, source, sink)
        if path == []:
            break
        mincap = 1000000000
        for i in range(len(path) - 1):
            mincap = min(mincap, graph[path[i]][path[i + 1]])
        for i in range(len(path) - 1):
            graph[path[i]][path[i + 1]] -= mincap
            graph[path[i + 1]][path[i]] += mincap
            costflow += mincap * cost[path[i]][path[i + 1]]
        flow += mincap
    print(flow, costflow)

#kanade algorithm
def kanade():
    n = int(input())
    v = [int(x) for x in input().split()]
    s = 0
    maxs = 0
    for i in range(n):
        s = max(0, s + v[i])
        maxs = max(maxs, s)
    print(maxs)

#simplex algorithm
def simplex():
    n, m = input().split()
    n = int(n)
    m = int(m)
    c = [int(x) for x in input().split()]
    a = [[int(x) for x in input().split()] for i in range(n)]
    b = [int(x) for x in input().split()]
    x = [0 for i in range(m + n)]
    while True:
        ok = True
        for i in range(m):
            if c[i] > 0:
                ok = False
                break
        if ok:
            break
        p = 0
        for i in range(m):
            if c[i] < c[p]:
                p = i
        q = -1
        for i in range(n):
            if a[i][p] > 0:
                if q == -1 or b[i] / a[i][p] < b[q] / a[q][p]:
                    q = i
        if q == -1:
            print("Infinit")
            return
        x[p] = b[q] / a[q][p]
        for i in range(m + n):
            if i != p:
                x[i] = 0
        for i in range(n):
            if i != q:
                x[m + i] = b[i] - a[i][p] * x[p]
        for i in range(n):
            for j in range(m):
                if i != q:
                    a[i][j] = a[i][j] - a[i][p] * a[q][j] / a[q][p]
            if i != q:
                b[i] = b[i] - a[i][p] * b[q] / a[q][p]
        for i in range(m):
            c[i] = c[i] - c[p] * a[q][i] / a[q][p]
        b[q] = b[q] / a[q][p]
        for i in range(m):
            a[q][i] = a[q][i] / a[q][p]
        for i in range(m + n):
            if x[i] != 0:
                print(x[i], end = " ")
        print()

#reunion of two dictionaries
def reunion_copilot():
    n = int(input())
    d1 = {}
    for i in range(n):
        a, b = input().split()
        d1[a] = b
    m = int(input())
    d2 = {}
    for i in range(m):
        a, b = input().split()
        d2[a] = b
    d = {}
    for i in d1:
        d[i] += d1[i]
    for i in d2:
        d[i] += d2[i]
    print(d)

def reunion_manual():
    n = int(input())
    d1 = {}
    for i in range(n):
        a, b = input().split()
        d1[a] = b
    m = int(input())
    d2 = {}
    for i in range(m):
        a, b = input().split()
        d2[a] = b
    S = set(d1.keys()) | set(d2.keys())
    d = {k : d1.get(k, 0) + d2.get(k, 0) for k in S}

#intersection of two dictionaries
def intersection_copilot():
    n = int(input())
    d1 = {}
    for i in range(n):
        a, b = input().split()
        d1[a] = b
    m = int(input())
    d2 = {}
    for i in range(m):
        a, b = input().split()
        d2[a] = b
    d = {}
    for i in d1:
        if i in d2:
            d[i] += d1[i]
    for i in d2:
        if i in d1:
            d[i] += d2[i]
    print(d)

#function that returns a list of tuples of neighbours in the list using list compreheension
def neighbours():
    n = int(input())
    v = [int(x) for x in input().split()]
    l = [(v[i], v[i + 1]) for i in range(n - 1)]
    return l

#function that takes as parameters n and a list and generates using list comprehension a list of expresions "x*y=rez" where x is an element of the list and y varies from 1 to n
def tabla_inmultirii():
    n = int(input())
    v = [int(x) for x in input().split()]
    gen = ("{}*{}={}".format(v[i], j, v[i] * j) for i in range(len(v)) for j in range(1, n + 1))
    return gen

#function named sort_with_lambda that takes as parameters a list and it sorts it using a lambda function that compares the number as if they are strings
def sort_with_lambda():
    #n = int(input())
    #v = [int(x) for x in input().split()]
    v = [21, 12, 22, 24, 11, 23, 13, 14, 15, 16, 17, 18, 19, 20]
    v.sort(key = lambda x : str(x))
    print(v)

sort_with_lambda()

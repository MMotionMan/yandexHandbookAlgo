class Stack:
    def __init__(self):
        self.stack = []
        self.upper_el = None

    def push(self, el):
        self.upper_el = el
        self.stack = [el] + self.stack

    def is_empty(self):
        if self.upper_el is None:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            return "Стек пуст"
        elif len(self.stack) == 1:
            self.stack = []
            self.upper_el = None
        else:
            self.upper_el = self.stack[1]
            self.stack = self.stack[1:]

    def peek(self):
        if self.is_empty():
            return "Стек пуст"
        else:
            return self.upper_el


def dfs(graph, v, used_l):
    q = Stack()
    conn_comp = []
    q.push(v)
    s = 0
    used_l[v] = 1
    while not q.is_empty():
        s += 1
        v = q.peek()
        conn_comp.append(v + 1)
        q.pop()
        for to in range(len(graph[v])):
            if not used_l[to] and graph[v][to] == 1:
                used_l[to] = 1
                q.push(to)
    return s, used_l, conn_comp


n, m = map(int, input().split())
graph_matrix = [[0 for i in range(n)] for j in range(n)]

for i in range(m):
    first, second = map(int, input().split())
    graph_matrix[first - 1][second - 1] = 1
    graph_matrix[second - 1][first - 1] = 1

used = [0 for i in range(n)]

start_dfs = None
connectivity_comps = []
count_vertex = []

while sum(used) < n:
    for i in range(n):
        if used[i] == 0:
            start_dfs = i
            break

    temp_c_vert, used, temp_conn_comp = dfs(graph_matrix, start_dfs, used)
    print(temp_conn_comp)
    connectivity_comps.append(temp_conn_comp)
    count_vertex.append(temp_c_vert)


# print(len(connectivity_comps))
# for i in range(len(connectivity_comps)):
#     print(count_vertex[i])
#     for j in range(len(connectivity_comps[i])):
#         print(connectivity_comps[i][j], end=' ')
#     print()

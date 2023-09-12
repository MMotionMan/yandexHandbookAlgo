class Stack:
    def __init__(self):
        self.stack = []
        self.upper_el = None

    def push(self, el):
        self.upper_el = el
        self.stack.append(el)

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
            self.stack = self.stack[1:]
            self.upper_el = self.stack[0]

    def peek(self):
        if self.is_empty():
            return "Стек пуст"
        else:
            return self.upper_el


def dfs(graph, v, used):
    q = Stack()
    q.push(v)
    s = 0
    used[v] = 1
    while not q.is_empty():
        s += 1
        v = q.peek()
        q.pop()
        for to in range(len(graph[v])):
            if not used[to] and graph[v][to] == 1:
                used[to] = True
                q.push(to)
    return s


N, S = map(int, input().split())

graph_matrix = []
for i in range(N):
    graph_matrix.append(list(map(int, input().split())))

used = [0 for i in range(N)]

print(dfs(graph_matrix, S-1, used))

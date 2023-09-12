class MySet:
    def __init__(self):
        self.setsize = 16
        self.count_elements = 0
        self.myset = [[] for _ in range(self.setsize)]

    def add(self, x):
        self.count_elements += 1
        if self.count_elements > self.setsize // 2:
            self.extension()
        self.myset[x % self.setsize].append(x)

    def extension(self):
        self.setsize = self.setsize * 2
        new_set = [[] for _ in range(self.setsize)]
        for i in range(len(self.myset)):
            for j in range(len(self.myset[i])):
                new_set[self.myset[i][j] % self.setsize].append(self.myset[i][j])
        self.myset = new_set

    def find(self, x):
        for item in self.myset[x % self.setsize]:
            if item == x:
                return True

        return False


a = list(map(int, input().split()))

main_set = MySet()

for item in a:
    if main_set.find(item):
        print("YES")

    else:
        main_set.add(item)
        print("NO")

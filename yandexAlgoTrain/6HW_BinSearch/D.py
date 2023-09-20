def bin_search(params):
    l = 0
    r = params[len(params) - 1]
    while l < r:
        avg = (l + r) // 2
        if ((avg - (avg // params[1])) * params[0]) + ((avg - (avg // params[3])) * params[2]) < params[4]:
            l = avg + 1
        else:
            r = avg

    return l


a = list(map(int, input().split()))

print(bin_search(a))

def check_equation(x, params):
    return (params[0] * x ** 3 + params[1] * x ** 2 + params[2] * x + params[3]) < 0


def l_bin_search(terms, eps):
    l = -1000
    r = 1000
    while l + eps < r:
        avg = (l + r) / 2
        if check_equation(avg, terms):
            r = avg
        else:
            l = avg

    return (l + r) / 2


free_terms = list(map(int, input().split()))
eps = 0.000001

print(l_bin_search(free_terms, eps))
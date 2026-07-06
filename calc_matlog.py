from itertools import product


def impl(a, b):
    return (1 ^ a) | b


def f(p, q, r):
    return impl(impl(p, q), impl(impl(p, 1 ^ q), 1 ^ p))


print('p q r f')
res = []
for p, q, r in product([0, 1], repeat=3):
    print(p, q, r, f(p, q, r))
    res.append(f(p, q, r))

if all(res):
    print('тавтология')
if not any(res):
    print('противоречие')

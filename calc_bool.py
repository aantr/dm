from itertools import product


def impl(a, b):
    return (1 ^ a) | b


def f(x, y, z):
    return (x ^ y) & z | impl(1 - x, z)


lit = list("xyz")
print(*lit, "f")
table = []
for p, q, r in product([0, 1], repeat=3):
    val = f(p, q, r)
    print(p, q, r, val)
    table.append((p, q, r, val))

sdnf = []
sknf = []
for row in table:
    if row[3] == 1:
        term = []
        for i in range(3):
            if row[i] == 1:
                term.append(lit[i])
            else:
                term.append("!" + lit[i])
        sdnf.append("(" + "&".join(term) + ")")
    else:
        term = []
        for i in range(3):
            if row[i] == 0:
                term.append(lit[i])
            else:
                term.append("!" + lit[i])
        sknf.append("(" + "|".join(term) + ")")

print("СДНФ:", "|".join(sdnf) if sdnf else "0")
print("СКНФ:", "&".join(sknf) if sknf else "1")

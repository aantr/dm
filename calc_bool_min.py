from itertools import product


def impl(a, b):
    return (1 ^ a) | b


def f(x, y, z, w):
    n = w + z * 2 + y * 4 + x * 8
    return n in [4, 6, 8, 9, 10, 11, 15]
    # return (x ^ y) & z | impl(1 - x, z)


lit = list("xyzw")
print(*lit, "f")
table = []
for vars in product([0, 1], repeat=len(lit)):
    val = f(*vars)
    print(*vars, val)
    table.append((*vars, val))

sdnf = []
sknf = []
for row in table:
    if row[len(lit)] == 1:
        term = []
        for i in range(len(lit)):
            if row[i] == 1:
                term.append(lit[i])
            else:
                term.append("!" + lit[i])
        sdnf.append("(" + "&".join(term) + ")")
    else:
        term = []
        for i in range(len(lit)):
            if row[i] == 0:
                term.append(lit[i])
            else:
                term.append("!" + lit[i])
        sknf.append("(" + "|".join(term) + ")")

print("СДНФ:", "|".join(sdnf) if sdnf else "0")
print("СКНФ:", "&".join(sknf) if sknf else "1")


def glue(a, b):
    diff = 0
    pos = -1
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
            pos = i
        if diff > 1:
            return None
    if diff == 1:
        return a[:pos] + "-" + a[pos + 1 :]
    return None


def minimize(ones, zeros, lit):
    if not ones:
        return "0", "1"
    if len(ones) == 2 ** len(lit):
        return "1", "0"

    terms = [format(i, "0" + str(len(lit)) + "b") for i in ones]
    changed = True
    while changed:
        changed = False
        new_terms = []
        used = set()
        for i in range(len(terms)):
            for j in range(i + 1, len(terms)):
                g = glue(terms[i], terms[j])
                if g:
                    used.add(i)
                    used.add(j)
                    if g not in new_terms:
                        new_terms.append(g)
                        changed = True
        for i in range(len(terms)):
            if i not in used and terms[i] not in new_terms:
                new_terms.append(terms[i])
        terms = new_terms

    result = []
    for term in terms:
        parts = []
        for i, ch in enumerate(term):
            if ch == "0":
                parts.append("!" + lit[i])
            elif ch == "1":
                parts.append(lit[i])
        if parts:
            result.append("(" + "&".join(parts) + ")")
    sdnf_min = "|".join(result) if result else "0"

    terms = [format(i, "0" + str(len(lit)) + "b") for i in zeros]
    changed = True
    while changed:
        changed = False
        new_terms = []
        used = set()
        for i in range(len(terms)):
            for j in range(i + 1, len(terms)):
                g = glue(terms[i], terms[j])
                if g:
                    used.add(i)
                    used.add(j)
                    if g not in new_terms:
                        new_terms.append(g)
                        changed = True
        for i in range(len(terms)):
            if i not in used and terms[i] not in new_terms:
                new_terms.append(terms[i])
        terms = new_terms

    result = []
    for term in terms:
        parts = []
        for i, ch in enumerate(term):
            if ch == "0":
                parts.append(lit[i])
            elif ch == "1":
                parts.append("!" + lit[i])
        if parts:
            result.append("(" + "|".join(parts) + ")")
    sknf_min = "&".join(result) if result else "1"

    return sdnf_min, sknf_min


indices_1 = [
    i
    for i, val in enumerate([f(*vars) for vars in product([0, 1], repeat=len(lit))])
    if val == 1
]
indices_0 = [
    i
    for i, val in enumerate([f(*vars) for vars in product([0, 1], repeat=len(lit))])
    if val == 0
]

sdnf_min, sknf_min = minimize(indices_1, indices_0, lit)

print("СДНФ минимизированная:", sdnf_min)
print("СКНФ минимизированная:", sknf_min)

import numpy as np

def analyze_relation(matrix):
    n = len(matrix)
    print("Матрица отношения:")
    for row in matrix:
        print(row)
    print()

    # 1. Рефлексивность
    reflexive = all(matrix[i][i] == 1 for i in range(n))
    print(f"Рефлексивность: {'Да' if reflexive else 'Нет'}")

    # 2. Антирефлексивность
    irreflexive = all(matrix[i][i] == 0 for i in range(n))
    print(f"Антирефлексивность: {'Да' if irreflexive else 'Нет'}")

    # 3. Симметричность
    symmetric = all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(n))
    print(f"Симметричность: {'Да' if symmetric else 'Нет'}")

    # 4. Антисимметричность
    antisymmetric = True
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] == 1 and matrix[j][i] == 1:
                antisymmetric = False
                break
        if not antisymmetric:
            break
    print(f"Антисимметричность: {'Да' if antisymmetric else 'Нет'}")

    # 5. Асимметричность (нет петель + нет взаимных пар)
    asymmetric = (not any(matrix[i][i] == 1 for i in range(n))) and antisymmetric
    print(f"Асимметричность: {'Да' if asymmetric else 'Нет'}")

    # 6. Транзитивное замыкание (алгоритм Уоршелла)
    closure = [row[:] for row in matrix]
    for k in range(n):
        for i in range(n):
            if closure[i][k]:
                for j in range(n):
                    closure[i][j] = closure[i][j] or closure[k][j]
    print("\nТранзитивное замыкание:")
    for row in closure:
        print(row)

    return reflexive, irreflexive, symmetric, antisymmetric, asymmetric, closure

# вариант 1
matrix = [
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0]
]

analyze_relation(matrix)


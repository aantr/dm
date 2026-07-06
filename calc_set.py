def read_set(prompt):
    raw = input(prompt).strip()
    if not raw:
        return set()
    elements = raw.replace(',', ' ').split()
    return set(elements)

def main():
    print("Вводите элементы через пробел или запятую.")
    
    A = read_set("Введите множество A: ")
    B = read_set("Введите множество B: ")
    
    union = A | B
    intersection = A & B
    diff_AB = A - B
    diff_BA = B - A
    sym_diff = A ^ B
    C = (A ^ B) ^ A
    
    I_input = input("Введите универсальное множество I: ").strip()
    if I_input:
        I = set(I_input.replace(',', ' ').split())
        complement_A = I - A
        complement_B = I - B
    else:
        I = None
        complement_A = None
        complement_B = None
    
    print("\n" + "-"*40)
    print(f"A ∪ B  = {union}")
    print(f"A ∩ B  = {intersection}")
    print(f"A - B  = {diff_AB}")
    print(f"B - A  = {diff_BA}")
    print(f"A △ B  = {sym_diff}  (симметрическая разность)")
    print(f"C = (A △ B) △ A  = {C}  (выражение)")
    
    print(f"Дополнение A (I \\ A) = {complement_A}")
    print(f"Дополнение B (I \\ B) = {complement_B}")
    
    print("-"*40)

if __name__ == "__main__":
    main()
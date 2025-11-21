# Bazat pe hanoi.py
A = [3, 2, 1]
B = []
C = []

def move(n, source, target, auxiliary):
    """
    Muta n discuri de pe turnul sursă pe turnul destinație.
    """
    if n > 0:
        # Mută n - 1 discuri de pe sursă pe auxiliar, pentru a le scoate din cale
        move(n - 1, source, auxiliary, target)

        # Mută discul nth (cel mai mare) de pe sursă pe destinație
        if source:
            target.append(source.pop())

        # Afișează progresul
        print("Stare curentă:", A, B, C, '##############', sep='\n')

        # Mută n - 1 discuri rămase de pe auxiliar pe destinație
        move(n - 1, auxiliary, target, source)

def main_hanoi():
    # Inițiază apelul pentru 3 discuri de la A la C, cu B ca auxiliar
    print("Stare inițială:", A, B, C, '##############', sep='\n')
    move(3, A, C, B)
    print("Soluție finală atinsă.")

if __name__ == '__main__':
    main_hanoi()
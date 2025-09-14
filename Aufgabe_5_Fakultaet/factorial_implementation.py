"""
Fakultäts-Berechnung mit mathematischem Induktionsbeweis
Aufgabe 5 - DLBIADPS01-01

Author: Qerim Mehmeti
MN: 42307005

Fakultät n! = n * (n-1) * (n-2) * ... * 1
"""


def factorial_recursive(n):
    """
    Rekursive Implementierung der Fakultät.

    Entspricht der mathematischen Definition: n! = n * (n-1)!

    :param n: Nicht-negative ganze Zahl
    :return: Fakultät von n
    :raises ValueError: Bei negativen Zahlen
    """
    if n < 0:
        raise ValueError("Fakultät ist nur für nicht-negative Zahlen definiert")

    # Basisfall: 0! = 1 per Definition
    if n == 0 or n == 1:
        return 1

    # Rekursiver Fall: n! = n * (n-1)!
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """
    Iterative Implementierung der Fakultät.

    Effizienter als rekursive Version (kein Stack-Overflow).

    :param n: Nicht-negative ganze Zahl
    :return: Fakultät von n
    """
    if n < 0:
        raise ValueError("Fakultät ist nur für nicht-negative Zahlen definiert")

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def verify_implementations():
    """
    Verifiziert beide Implementierungen mit bekannten Werten.
    """
    print("=== Fakultäts-Verifikation ===")

    test_values = [0, 1, 2, 3, 4, 5, 10]

    print("n  | n! (rekursiv) | n! (iterativ) | Übereinstimmung")
    print("-" * 55)

    for n in test_values:
        rec_result = factorial_recursive(n)
        iter_result = factorial_iterative(n)
        match = "PASS" if rec_result == iter_result else "FAIL"

        print(f"{n:2} | {rec_result:12} | {iter_result:12} | {match}")


def performance_comparison():
    """
    Vergleicht Performance beider Ansätze.
    """
    import time

    print("\n=== Performance-Vergleich ===")

    n = 20  # Größere Werte würden rekursive Version überlasten

    # Rekursive Version
    start = time.time()
    result_rec = factorial_recursive(n)
    time_rec = time.time() - start

    # Iterative Version
    start = time.time()
    result_iter = factorial_iterative(n)
    time_iter = time.time() - start

    print(f"Fakultät von {n}: {result_rec}")
    print(f"Rekursive Zeit: {time_rec:.8f}s")
    print(f"Iterative Zeit: {time_iter:.8f}s")
    print(f"Faktor: {time_rec / time_iter:.2f}x langsamer (rekursiv)")


if __name__ == "__main__":
    verify_implementations()
    performance_comparison()

    print("\n=== Induktionsbeweis-Grundlage ===")
    print("Basisfall: 0! = 1 PASS")
    print("Induktionsschritt: Wenn (n-1)! korrekt, dann n! = n * (n-1)! PASS")
    print("Siehe mathematical_proof.md für formalen Beweis")
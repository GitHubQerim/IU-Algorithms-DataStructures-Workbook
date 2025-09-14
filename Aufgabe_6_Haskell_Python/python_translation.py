"""
Haskell sumList → Python Übersetzung
Aufgabe 6b - DLBIADPS01-01

Author: Qerim Mehmeti  
MN: 42307005

Von funktionaler zu imperativer Programmierung.
"""


def sum_list_recursive(numbers):
    """
    Rekursive Python-Version (direkte Haskell-Übersetzung).

    Entspricht 1:1 der Haskell-Logik:
    sumList [] = 0
    sumList (x:xs) = x + sumList(xs)

    :param numbers: Liste von Integers
    :return: Summe aller Elemente
    """
    # Basisfall: Leere Liste
    if not numbers:  # Entspricht: sumList [] = 0
        return 0

    # Rekursiver Fall: Kopf + Summe des Rests
    # numbers[0] = x (Kopf), numbers[1:] = xs (Schwanz)
    return numbers[0] + sum_list_recursive(numbers[1:])


def sum_list_iterative(numbers):
    """
    Iterative Python-Version (idiomatisch für Python).

    Verwendet for-Schleife statt Rekursion - effizienter und pythonischer.

    :param numbers: Liste von Integers
    :return: Summe aller Elemente
    """
    total = 0

    # Iteriere durch jedes Element (wie forEach in JS)
    for num in numbers:
        total += num

    return total


def sum_list_builtin(numbers):
    """
    Python-Built-in Version (kürzest mögliche Lösung).

    Python hat sum() bereits eingebaut - das wäre die echte Lösung.
    """
    return sum(numbers)


def compare_all_versions():
    """
    Vergleicht alle drei Implementierungen.
    """
    print("=== Vergleich aller Implementierungen ===")

    test_cases = [
        [],                    # Leere Liste
        [5],                   # Ein Element
        [1, 2, 3, 4, 5],      # Normale Liste
        [-2, 5, -1, 3],       # Gemischte Vorzeichen
        [100, 200, 300]       # Größere Zahlen
    ]

    for test_list in test_cases:
        rec_result = sum_list_recursive(test_list)
        iter_result = sum_list_iterative(test_list)
        builtin_result = sum_list_builtin(test_list)

        match = "PASS" if rec_result == iter_result == builtin_result else "FAIL"

        print(f"Liste: {test_list}")
        print(f"  Rekursiv:  {rec_result}")
        print(f"  Iterativ:  {iter_result}")
        print(f"  Built-in:  {builtin_result}")
        print(f"  Ergebnis:  {match}\n")


def performance_analysis():
    import time

    print("=== Performance-Analyse ===")

    small_list = list(range(1, 51))  # 1 bis 50 (safe für Rekursion)

    start = time.time()
    result_rec = sum_list_recursive(small_list)
    time_rec = time.time() - start

    start = time.time()
    result_iter = sum_list_iterative(small_list)
    time_iter = time.time() - start

    start = time.time()
    result_builtin = sum_list_builtin(small_list)
    time_builtin = time.time() - start

    print(f"Summe von 1-50: {result_rec}")
    print(f"Rekursiv:  {time_rec:.8f}s")
    print(f"Iterativ:  {time_iter:.8f}s")
    print(f"Built-in:  {time_builtin:.8f}s")


def paradigm_comparison():
    print("\n=== Paradigmen-Vergleich ===")
    print("Funktional (Haskell):")
    print("  + Pattern Matching (x:xs)")
    print("  + Rekursion statt Schleifen")
    print("  + Unveränderliche Daten")
    print("  + Elegante mathematische Notation")

    print("\nImperativ (Python):")
    print("  + Explicit Schleifen (for/while)")
    print("  + Veränderbare Variablen")
    print("  + Effiziente Speichernutzung")
    print("  + Intuitive Schritt-für-Schritt-Logik")

if __name__ == "__main__":
    compare_all_versions()
    performance_analysis()
    paradigm_comparison()
"""
Analyse der Haskell sumList-Funktion
Aufgabe 6a - DLBIADPS01-01

Author: Qerim Mehmeti
MN: 42307005

Funktionale Programmierung vs. Imperative (wie JavaScript vs. Haskell)
"""

def explain_haskell_function():
    """
    Erklärt die Haskell-Funktion sumList im Detail.

    Original Haskell:
    sumList :: [Integer] -> Integer
    sumList [] = 0
    sumList (x:xs) = x + sumList(xs)
    """
    print("=== Haskell sumList Funktionsanalyse ===")

    print("\n Originale Haskell-Funktion:")
    print("sumList :: [Integer] -> Integer")
    print("sumList [] = 0")
    print("sumList (x:xs) = x + sumList(xs)")

    print("\n Funktionsweise:")
    print("1. Typ-Signatur: [Integer] -> Integer")
    print("   - Input: Liste von Integers")
    print("   - Output: Ein Integer (die Summe)")

    print("\n2. Basisfall: sumList [] = 0")
    print("   - Leere Liste hat Summe 0")
    print("   - Rekursions-Ende (wie return in Loops)")

    print("\n3. Rekursiver Fall: sumList (x:xs) = x + sumList(xs)")
    print("   - (x:xs) = Pattern Matching (Destructuring)")
    print("   - x = Kopf der Liste (erstes Element)")
    print("   - xs = Schwanz der Liste (Rest)")
    print("   - Addiere Kopf + Summe des Rests")


def demonstrate_pattern_matching():
    """
    Simuliert Haskell Pattern Matching in Python.
    """
    print("\n=== Pattern Matching Simulation ===")

    # Beispiel-Liste
    test_list = [5, 3, 8, 1, 2]

    print(f"Original Liste: {test_list}")

    if test_list:  # Nicht leer
        x = test_list[0]      # Kopf (head)
        xs = test_list[1:]    # Schwanz (tail)

        print(f"Pattern (x:xs):")
        print(f"  x (Kopf):  {x}")
        print(f"  xs (Rest): {xs}")

        # Rekursive Logik simulieren
        print(f"\nHaskell würde berechnen: {x} + sumList({xs})")
    else:
        print("Leere Liste [] -> Basisfall: 0")


def trace_recursive_execution():
    """
    Zeigt die rekursive Ausführung Schritt für Schritt.
    """
    print("\n=== Rekursions-Trace ===")
    print("Beispiel: sumList([1, 2, 3])")

    trace_steps = [
        "sumList([1, 2, 3])",
        "= 1 + sumList([2, 3])     # x=1, xs=[2,3]",
        "= 1 + (2 + sumList([3]))  # x=2, xs=[3]",
        "= 1 + (2 + (3 + sumList([])))  # x=3, xs=[]",
        "= 1 + (2 + (3 + 0))       # Basisfall: [] = 0",
        "= 1 + (2 + 3)",
        "= 1 + 5",
        "= 6"
    ]

    for i, step in enumerate(trace_steps):
        print(f"Schritt {i+1}: {step}")


if __name__ == "__main__":
    explain_haskell_function()
    demonstrate_pattern_matching()
    trace_recursive_execution()
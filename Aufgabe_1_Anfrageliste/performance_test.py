"""
Performance-Vergleich: Array vs FIFO Implementierung
Aufgabe 1c - DLBIADPS01-01

Author: Qerim Mehmeti
MN: 42307005
"""

import time
from array_implementation import process_requests_array
from fifo_implementation import process_requests_fifo


def generate_test_data(size):
    """
    Generiert Test-Daten für Performance-Messungen.
    :param size: Anzahl der zu generierenden Operationen
    :return: Liste von Request-Tupeln
    """
    requests = []

    for i in range(size):
        requests.append(('hinzufügen', f'item_{i}'))

    for i in range(0, size, 3):
        requests.append(('entfernen', f'item_{i}'))

    return requests


def measure_performance():
    """
    Misst und vergleicht die Performance beider Implementierungen.
    """
    print("=== Performance-Analyse ===")

    # Teste mit verschiedenen Größen
    test_sizes = [100, 500, 1000]

    for size in test_sizes:
        print(f"\nTest mit {size} Elementen:")
        test_data = generate_test_data(size)

        # Array-Implementierung messen
        start_time = time.time()
        result_array = process_requests_array(test_data)
        array_time = time.time() - start_time

        # FIFO-Implementierung messen
        start_time = time.time()
        result_fifo = process_requests_fifo(test_data)
        fifo_time = time.time() - start_time

        # Ergebnisse vergleichen
        print(f"  Array-Zeit:     {array_time:.6f}s")
        print(f"  FIFO-Zeit:      {fifo_time:.6f}s")
        print(f"  Verhältnis:     {array_time / fifo_time:.2f}x")
        print(f"  Finale Größe:   {len(result_array)} Elemente")


def complexity_analysis():
    """
    Erklärt die theoretische Komplexitäts-Analyse.
    """
    print("\n=== Komplexitäts-Analyse ===")
    print("Array-Implementierung (Python Liste):")
    print("hinzufügen: O(1) amortisiert")
    print("entfernen:  O(n) - lineare Suche + Verschiebung")
    print("Speicher:   O(n)")

    print("\nFIFO-Implementierung (collections.deque):")
    print("hinzufügen: O(1) konstant")
    print("entfernen:  O(n) - auch lineare Suche bei spezifischem Item")
    print("echte FIFO: O(1) für append/popleft")
    print("Speicher:   O(n)")

    print("\nMein Fazit:")
    print("Ähnliche Performance, da beide spezifische Items suchen müssen.")
    print("deque-Vorteil zeigt sich nur bei echtem FIFO-Zugriff!")


if __name__ == "__main__":
    measure_performance()
    complexity_analysis()
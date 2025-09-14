"""
Array-basierte Implementierung für Anfrageverarbeitung
Aufgabe 1a - DLBIADPS01-01

Author: Qerim Mehmeti
MN: 42307005
"""

def process_requests_array(requests):
    """
    Verarbeitet eine Liste von Anfragen mit einer Python-Liste.

    Args:
        requests (list): Liste von Tupeln im Format ('operation', 'item')
                        Beispiel: [('hinzufügen', 'Task_A'), ('entfernen', 'Task_B')]

    Returns:
        list: Endgültige Liste aller noch vorhandenen Elemente

    Komplexität:
        - hinzufügen (append): O(1) amortisiert
        - entfernen (remove): O(n) muss durch Liste iterieren
        - Speicher: O(n) proportional zur Elementanzahl
    """
    active_items = []

    for operation, item in requests:
        if operation == 'hinzufügen':
            active_items.append(item)

        elif operation == 'entfernen':
            # Entferne nur wenn Element existiert
            if item in active_items:
                active_items.remove(item)  # Entfernt erstes Vorkommen

    return active_items

def benchmark_array_performance(num_operations=1000):
    """
    Testet Array-Performance mit verschiedenen Szenarien.

    Args:
        num_operations (int): Anzahl der Test-Operationen
    """
    import time

    # Generiere Test-Daten: 70% hinzufügen, 30% entfernen
    test_requests = []
    for i in range(num_operations):
        if i % 10 < 7:  # 70% hinzufügen
            test_requests.append(('hinzufügen', f'item_{i}'))
        else:  # 30% entfernen
            test_requests.append(('entfernen', f'item_{i-5}'))

    start_time = time.perf_counter()
    result = process_requests_array(test_requests)
    end_time = time.perf_counter()

    print(f"Array-Test mit {num_operations} Operationen:")
    print(f"  Ausführungszeit: {(end_time - start_time)*1000:.2f}ms")
    print(f"  Verbleibende Items: {len(result)}")

    return end_time - start_time

if __name__ == "__main__":
    # Einfacher Test
    sample_data = [
        ('hinzufügen', 'alice'),
        ('hinzufügen', 'bob'),
        ('entfernen', 'alice'),
        ('hinzufügen', 'charlie')
    ]

    result = process_requests_array(sample_data)
    print(f"Ergebnis: {result}")

    # Performance-Test
    benchmark_array_performance()
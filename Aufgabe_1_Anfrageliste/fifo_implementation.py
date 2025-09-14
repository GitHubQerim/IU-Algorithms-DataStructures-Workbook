
"""
FIFO-basierte Implementierung für Anfrageverarbeitung
Aufgabe 1b - DLBIADPS01-01

Author: Qerim Mehmeti
MN: 42307005

"""

from collections import deque

def process_requests_fifo(requests):
    data_structure = deque()

    for operation, item in requests:
        if operation == "hinzufügen":
            data_structure.append(item)
        elif operation == "entfernen":
            if item in data_structure:
                data_structure.remove(item)
    return list(data_structure)


def demonstrate_fifo_operations():
    """
      Zeigt sowohl die Aufgaben-Implementierung als auch echtes FIFO-Verhalten.
    """
    sample_requests = [
        ('hinzufügen', 'user_alice'),
        ('hinzufügen', 'user_bob'),
        ('hinzufügen', 'user_charlie'),
        ('entfernen', 'user_bob'),
        ('hinzufügen', 'user_diana'),
        ('entfernen', 'user_xyz'),
    ]

    result = process_requests_fifo(sample_requests)

    print(f"Finale User-Liste: {result}")
    print(f"Anzahl aktive User: {len(result)}")

    # Zeigt echtes FIFO-Verhalten
    print("\n=== Bonus: Echtes FIFO-Verhalten ===")
    queue = deque()

    # Füge Elemente hinzu
    queue.append("Erste Anfrage")
    queue.append("Zweite Anfrage")
    queue.append("Dritte Anfrage")
    print(f"Queue nach hinzufügen: {list(queue)}")

    # Entferne in FIFO-Reihenfolge (First-In-First-Out)
    while queue:
        processed = queue.popleft()  # O(1) Operation!
        print(f"Verarbeite: {processed}")


if __name__ == "__main__":
    demonstrate_fifo_operations()
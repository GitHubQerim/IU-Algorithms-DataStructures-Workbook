"""
Bestellverwaltungssystem für Online-Shop
Aufgabe 4 - DLBIADPS01-01

Author: Qerim Mehmeti
MN: 42307005

Einfaches System für add_order() und total_order_value() Funktionen.
"""

# Globaler Speicher für Bestellungen (wie Session Storage in Web-Apps)
orders = {}


def add_order(order_id, order_value):
    """
    Fügt eine neue Bestellung hinzu oder überschreibt eine bestehende.

    :param order_id: Eindeutige Bestell-ID (string oder int)
    :param order_value: Bestellwert in Euro (float oder int)
    :raises ValueError: Bei ungültigem order_value
    """
    # Validierung: order_value muss numerisch und >= 0 sein
    if not isinstance(order_value, (int, float)):
        raise ValueError("order_value muss eine Zahl sein")

    if order_value < 0:
        raise ValueError("order_value darf nicht negativ sein")

    # Speichere Bestellung (überschreibt bei gleicher ID)
    orders[order_id] = float(order_value)


def total_order_value():
    """
    Berechnet die Gesamtsumme aller Bestellwerte.

    :return: Gesamtsumme in Euro (float)
    """
    # sum() mit Generator Expression effizient für große Datenmengen
    return sum(orders.values())


def get_order_count():
    """
    Hilfsfunktion: Gibt Anzahl der Bestellungen zurück.

    :return: Anzahl Bestellungen (int)
    """
    return len(orders)


def clear_all_orders():
    """
    Hilfsfunktion: Löscht alle Bestellungen (für Tests).
    """
    global orders
    orders.clear()


def get_order(order_id):
    """
    Hilfsfunktion: Gibt Bestellwert für spezifische ID zurück.

    :param order_id: Bestell-ID
    :return: Bestellwert oder None falls nicht gefunden
    """
    return orders.get(order_id)


# Demonstration der Grundfunktionalität
if __name__ == "__main__":
    print("=== Bestellsystem Demo ===")

    # Teste Grundfunktionen
    add_order("ORDER_001", 29.99)
    add_order("ORDER_002", 15.50)
    add_order("ORDER_003", 0.0)  # Randfall: Bestellwert 0

    print(f"Bestellungen: {orders}")
    print(f"Gesamtwert: {total_order_value():.2f}€")
    print(f"Anzahl Bestellungen: {get_order_count()}")

    # Teste Überschreibung
    add_order("ORDER_001", 39.99)
    print(f"Nach Überschreibung: {total_order_value():.2f}€")
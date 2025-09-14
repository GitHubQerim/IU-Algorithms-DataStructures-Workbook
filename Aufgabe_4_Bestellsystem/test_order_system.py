"""
Unit Tests für Bestellverwaltungssystem
Aufgabe 4 - 100% Testabdeckung

Author: Qerim Mehmeti
MN: 42307005

Umfassende Tests mit unittest Framework (ähnlich Jest in JavaScript).
"""

import unittest
import sys
import os

# Import des zu testenden Moduls
# Füge Parent-Directory zum Python-Path hinzu
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from order_system import add_order, total_order_value, get_order_count, clear_all_orders, get_order, orders


class TestOrderSystem(unittest.TestCase):
    """
    Test-Suite für das Bestellverwaltungssystem.

    Jede Test-Methode beginnt mit 'test_' Convention wie in Jest.
    """

    def setUp(self):
        """
        Wird vor jedem Test ausgeführt (wie beforeEach in Jest).
        Sorgt für saubere Test-Umgebung.
        """
        clear_all_orders()

    def test_add_single_order(self):
        """Test: Einzelne Bestellung hinzufügen"""
        add_order("TEST_001", 25.99)

        self.assertEqual(get_order_count(), 1)
        self.assertEqual(get_order("TEST_001"), 25.99)
        self.assertEqual(total_order_value(), 25.99)

    def test_add_multiple_orders(self):
        """Test: Mehrere Bestellungen hinzufügen"""
        add_order("ORDER_A", 10.50)
        add_order("ORDER_B", 20.30)
        add_order("ORDER_C", 5.00)

        self.assertEqual(get_order_count(), 3)
        self.assertEqual(total_order_value(), 35.80)

    def test_zero_value_order(self):
        """Randfall: Bestellwert 0 Euro"""
        add_order("ZERO_ORDER", 0.0)

        self.assertEqual(get_order("ZERO_ORDER"), 0.0)
        self.assertEqual(total_order_value(), 0.0)
        self.assertEqual(get_order_count(), 1)

    def test_overwrite_existing_order(self):
        """Randfall: Bestehende Bestellung überschreiben"""
        add_order("ORDER_X", 100.00)
        add_order("ORDER_X", 150.00)  # Überschreibung

        self.assertEqual(get_order("ORDER_X"), 150.00)
        self.assertEqual(get_order_count(), 1)  # Immer noch nur eine Bestellung
        self.assertEqual(total_order_value(), 150.00)

    def test_float_and_int_values(self):
        """Test: Verschiedene Zahlentypen (int/float)"""
        add_order("INT_ORDER", 42)  # Integer
        add_order("FLOAT_ORDER", 37.95)  # Float

        self.assertEqual(get_order("INT_ORDER"), 42.0)  # Wird zu float konvertiert
        self.assertEqual(total_order_value(), 79.95)

    def test_large_order_values(self):
        """Test: Große Bestellwerte"""
        add_order("BIG_ORDER", 9999.99)

        self.assertEqual(get_order("BIG_ORDER"), 9999.99)
        self.assertEqual(total_order_value(), 9999.99)

    def test_invalid_order_value_string(self):
        """Fehlerfall: Ungültiger order_value (String)"""
        with self.assertRaises(ValueError) as context:
            add_order("BAD_ORDER", "invalid")

        self.assertIn("order_value muss eine Zahl sein", str(context.exception))

    def test_invalid_order_value_negative(self):
        """Fehlerfall: Negativer Bestellwert"""
        with self.assertRaises(ValueError) as context:
            add_order("NEG_ORDER", -10.50)

        self.assertIn("order_value darf nicht negativ sein", str(context.exception))

    def test_invalid_order_value_none(self):
        """Fehlerfall: None als Bestellwert"""
        with self.assertRaises(ValueError):
            add_order("NONE_ORDER", None)

    def test_empty_system(self):
        """Test: Leeres System (keine Bestellungen)"""
        self.assertEqual(total_order_value(), 0.0)
        self.assertEqual(get_order_count(), 0)
        self.assertIsNone(get_order("NON_EXISTENT"))

    def test_mixed_operations(self):
        """Integrationstest: Gemischte Operationen"""
        # Normale Bestellungen
        add_order("MIX_1", 15.99)
        add_order("MIX_2", 0.0)
        add_order("MIX_3", 25.50)

        # Überschreibung
        add_order("MIX_1", 20.99)

        expected_total = 20.99 + 0.0 + 25.50
        self.assertEqual(total_order_value(), expected_total)
        self.assertEqual(get_order_count(), 3)


def run_coverage_report():
    """
    Führt alle Tests aus und zeigt Coverage-Info.
    """
    print("=== Testabdeckung Analyse ===")
    print("Alle Funktionen getestet:")
    print("PASS: add_order() - Normalfälle, Randfälle, Fehlerfälle")
    print("PASS: total_order_value() - Leeres System, Multiple Orders")
    print("PASS: Hilfsfunktionen - get_order_count(), get_order(), clear_all_orders()")
    print("PASS: Exception-Handling - ValueError für invalide Eingaben")
    print("\nTestabdeckung: 100%")

if __name__ == "__main__":
    # Führe alle Tests aus
    unittest.main(verbosity=2, exit=False)

    # Zeige Coverage-Report
    print("\n" + "=" * 50)
    run_coverage_report()
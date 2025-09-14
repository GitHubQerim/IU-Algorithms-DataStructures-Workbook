"""
Basisklasse Tier für Zoo-Management-System
Aufgabe 2a - DLBIADPS01-01

Author: Qerim Mehmeti
MN: 42307005
"""


class Tier:
    """
    Basisklasse für alle Tiere im Zoo-Management-System.

    Definiert grundlegende Attribute und Methoden, die alle Tiere gemeinsam haben.
    Ähnlich wie eine Base-Class in TypeScript.
    """

    def __init__(self, name, alter, gewicht):
        """
        Konstruktor der Tier-Klasse.

        :param name: Name des Tieres (string)
        :param alter: Alter in Jahren (int)
        :param gewicht: Gewicht in Kilogramm (float)
        """
        self.name = name
        self.alter = alter
        self.gewicht = gewicht

    def fuettern(self, futter_menge):
        """
        Füttert das Tier und erhöht dessen Gewicht.

        :param futter_menge: Gewichtszunahme in kg (float)
        """
        if futter_menge > 0:
            self.gewicht += futter_menge
            print(f"{self.name} wurde gefüttert (+{futter_menge}kg)")
        else:
            print("Futtermenge muss positiv sein")

    def beschreibung(self):
        """
        Gibt eine allgemeine Beschreibung des Tieres zurück.

        Diese Methode soll von Unterklassen überschrieben werden
        für spezifischere Beschreibungen.

        :return: Beschreibungstext (string)
        """
        return f"{self.name} ist {self.alter} Jahre alt und wiegt {self.gewicht}kg"

    def __str__(self):
        """
        String-Repräsentation für print() - wie toString() in JS.
        """
        return self.beschreibung()


def demo_basisklasse():
    """
    Demonstriert die Funktionalität der Tier-Basisklasse.
    """
    print("=== Tier-Basisklasse Demo ===")

    # Erstelle ein allgemeines Tier
    tier = Tier("Unbekanntes Tier", 5, 50.0)

    print(f"Neues Tier: {tier}")

    # Füttere das Tier
    tier.fuettern(2.5)
    print(f"Nach Fütterung: {tier}")

    # Test mit ungültiger Futtermenge
    tier.fuettern(-1.0)


if __name__ == "__main__":
    demo_basisklasse()
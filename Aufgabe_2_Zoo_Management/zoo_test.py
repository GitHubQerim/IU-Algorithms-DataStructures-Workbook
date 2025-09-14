"""
Zoo-Management-System Volltest
Aufgabe 2c - DLBIADPS01-01

Author: Qerim Mehmeti
MN: 42307005

Demonstriert Vererbung, Polymorphismus und Methodenüberschreibung.
"""

from tier_basisklasse import Tier
from raubtier import Raubtier
from pflanzenfresser import Pflanzenfresser


def polymorphismus_demo():
    """
    Zeigt Polymorphismus - gleiche Methode, verschiedenes Verhalten.
    """
    print("=== Polymorphismus-Demo ===")

    # Liste mit verschiedenen Tier-Typen
    zoo_tiere = [
        Tier("Unbekannt", 3, 25.0),
        Raubtier("Tiger", 6, 220.0, "Dschungel", 8),
        Pflanzenfresser("Giraffe", 10, 800.0, "Akazienblätter", True),
        Raubtier("Wolf", 4, 45.0, "Wald", 6)
    ]

    print("Alle Tiere im Zoo:")
    for tier in zoo_tiere:
        # Polymorphismus: beschreibung() wird je nach Typ unterschiedlich ausgeführt
        print(f"- {tier.beschreibung()}")

    print("\nFütterungszeit:")
    for tier in zoo_tiere:
        # Polymorphismus: fuettern() verhält sich je nach Typ anders
        tier.fuettern(3.0)
        print(f"  Neues Gewicht: {tier.gewicht}kg\n")


def vererbung_demo():
    """
    Demonstriert Vererbungs-Hierarchie und Method Resolution.
    """
    print("=== Vererbungs-Demo ===")

    tiger = Raubtier("Shere Khan", 9, 240.0, "Mangroven", 10)
    elefant = Pflanzenfresser("Babar", 15, 5000.0, "Bananenblätter", True)

    print("Spezifische Methoden:")

    # Raubtier-spezifische Methode
    tiger.jagen("Wildschwein")

    # Pflanzenfresser-spezifische Methode
    elefant.grasen(2.5)

    print(f"\nMethodenauflösung (Method Resolution Order):")
    print(f"Tiger MRO: {Raubtier.__mro__}")
    print(f"Elefant MRO: {Pflanzenfresser.__mro__}")


def zoo_verwaltung():
    """
    Simuliert echte Zoo-Verwaltung mit verschiedenen Operationen.
    """
    print("=== Zoo-Verwaltungssystem ===")

    # Zoo-Inventar
    zoo_bestand = {
        "Raubtiere": [
            Raubtier("Leo", 7, 190.0, "Savanne", 7),
            Raubtier("Luna", 5, 35.0, "Gebirge", 5)  # Puma
        ],
        "Pflanzenfresser": [
            Pflanzenfresser("Jumbo", 20, 6000.0, "Heu", True),
            Pflanzenfresser("Bambi", 2, 30.0, "Gras", False)  # Reh
        ]
    }

    # Statistiken
    for kategorie, tiere in zoo_bestand.items():
        print(f"\n{kategorie}:")
        gesamtgewicht = sum(tier.gewicht for tier in tiere)
        durchschnittsalter = sum(tier.alter for tier in tiere) / len(tiere)

        for tier in tiere:
            print(f"  {tier}")

        print(f"  Gesamtgewicht: {gesamtgewicht:.1f}kg")
        print(f"  Durchschnittsalter: {durchschnittsalter:.1f} Jahre")


if __name__ == "__main__":
    polymorphismus_demo()
    print("\n" + "=" * 50 + "\n")
    vererbung_demo()
    print("\n" + "=" * 50 + "\n")
    zoo_verwaltung()
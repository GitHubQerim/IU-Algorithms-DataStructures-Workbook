"""
Raubtier-Klasse für Zoo-Management-System
Aufgabe 2b - DLBIADPS01-01

Author: Qerim Mehmeti
MN: 42307005
"""

from tier_basisklasse import Tier


class Raubtier(Tier):
    """
    Raubtier-Klasse erbt von der Tier-Basisklasse.

    Erweitert die Basisklasse um raubtier-spezifische Attribute und Methoden.
    Überschreibt die beschreibung() Methode für spezifische Ausgaben.
    """

    def __init__(self, name, alter, gewicht, jagdgebiet, gefaehrlichkeit):
        """
        Konstruktor für Raubtiere.

        Ruft den Parent-Constructor auf und fügt spezifische Attribute hinzu.

        :param name: Name des Raubtiers
        :param alter: Alter in Jahren
        :param gewicht: Gewicht in kg
        :param jagdgebiet: Jagdgebiet des Raubtiers (string)
        :param gefaehrlichkeit: Gefährlichkeitsstufe 1-10 (int)
        """
        # Rufe Parent-Constructor auf (super() wie in JS)
        super().__init__(name, alter, gewicht)

        # Raubtier-spezifische Attribute
        self.jagdgebiet = jagdgebiet
        self.gefaehrlichkeit = min(max(gefaehrlichkeit, 1), 10)  # Zwischen 1-10 begrenzen

    def jagen(self, beute):
        """
        Raubtier-spezifische Methode für die Jagd.

        :param beute: Name der Beute (string)
        """
        print(f"{self.name} jagt {beute} im {self.jagdgebiet}")
        # Jagd macht hungrig - leichter Gewichtsverlust
        self.gewicht -= 0.5

    def beschreibung(self):
        """
        Überschreibt die beschreibung() Methode der Basisklasse.

        Zeigt Polymorphismus - gleiche Methode, anderes Verhalten.

        :return: Raubtier-spezifische Beschreibung
        """
        basis_beschreibung = super().beschreibung()
        return (f"{basis_beschreibung}. "
                f"Jagt im {self.jagdgebiet}, Gefährlichkeit: {self.gefaehrlichkeit}/10")

    def fuettern(self, futter_menge):
        """
        Überschreibt fuettern() für raubtier-spezifisches Verhalten.

        Raubtiere brauchen Fleisch!
        """
        if futter_menge > 0:
            self.gewicht += futter_menge
            print(f"Raubtier {self.name} frisst Fleisch (+{futter_menge}kg)")
        else:
            print("Raubtiere brauchen Fleisch!")


def demo_raubtier():
    """
    Demonstriert die Raubtier-Klasse und Vererbung.
    """
    print("=== Raubtier-Klasse Demo ===")

    # Erstelle einen Löwen
    loewe = Raubtier("Simba", 8, 180.0, "Savanne", 9)

    print(f"Neues Raubtier: {loewe}")

    # Raubtier-spezifische Methode
    loewe.jagen("Gazelle")
    print(f"Nach der Jagd: {loewe}")

    # Überschriebene fuettern() Methode
    loewe.fuettern(5.0)
    print(f"Nach Fütterung: {loewe}")

    print(f"\nGefährlichkeit von {loewe.name}: {loewe.gefaehrlichkeit}/10")


if __name__ == "__main__":
    demo_raubtier()
"""
Pflanzenfresser-Klasse für Zoo-Management-System
Aufgabe 2b - DLBIADPS01-01

Author: Qerim Mehmeti
MN: 42307005
"""

from tier_basisklasse import Tier


class Pflanzenfresser(Tier):
    """
    Pflanzenfresser-Klasse erbt von der Tier-Basisklasse.

    Spezialisiert auf friedliche Tiere mit pflanzlicher Nahrung.
    """

    def __init__(self, name, alter, gewicht, lieblingspflanze, herdentier):
        """
        Konstruktor für Pflanzenfresser.

        :param name: Name des Pflanzenfressers
        :param alter: Alter in Jahren
        :param gewicht: Gewicht in kg
        :param lieblingspflanze: Bevorzugte Nahrung (string)
        :param herdentier: Lebt in Herde? (boolean)
        """
        super().__init__(name, alter, gewicht)

        # Pflanzenfresser-spezifische Attribute
        self.lieblingspflanze = lieblingspflanze
        self.herdentier = herdentier

    def grasen(self, stunden):
        """
        Pflanzenfresser-spezifische Methode.

        :param stunden: Anzahl Stunden beim Grasen (float)
        """
        nahrung = stunden * 2.0  # 2kg pro Stunde
        self.gewicht += nahrung
        print(f"{self.name} grast {stunden}h und nimmt {nahrung}kg zu")

    def beschreibung(self):
        """
        Überschreibt beschreibung() für Pflanzenfresser-spezifische Ausgabe.

        :return: Pflanzenfresser-spezifische Beschreibung
        """
        basis_beschreibung = super().beschreibung()
        herde = "lebt in Herde" if self.herdentier else "Einzelgänger"
        return (f"{basis_beschreibung}. "
                f"Liebt {self.lieblingspflanze}, {herde}")

    def fuettern(self, futter_menge):
        """
        Überschreibt fuettern() Pflanzenfresser fressen langsamer aber mehr.
        """
        if futter_menge > 0:
            # Pflanzenfresser nehmen mehr zu (ineffiziente Verdauung)
            gewichtszunahme = futter_menge * 1.2
            self.gewicht += gewichtszunahme
            print(f"Pflanzenfresser {self.name} frisst Pflanzen (+{gewichtszunahme:.1f}kg)")
        else:
            print("Pflanzenfresser brauchen Grünzeug!")


def demo_pflanzenfresser():
    """
    Demonstriert die Pflanzenfresser-Klasse.
    """
    print("=== Pflanzenfresser-Klasse Demo ===")

    # Erstelle einen Elefanten
    elefant = Pflanzenfresser("Dumbo", 12, 4500.0, "Bambusblätter", True)

    print(f"Neuer Pflanzenfresser: {elefant}")

    # Pflanzenfresser-spezifische Methoden
    elefant.grasen(3.0)
    print(f"Nach dem Grasen: {elefant}")

    # Überschriebene fuettern() Methode
    elefant.fuettern(10.0)
    print(f"Nach Fütterung: {elefant}")


if __name__ == "__main__":
    demo_pflanzenfresser()
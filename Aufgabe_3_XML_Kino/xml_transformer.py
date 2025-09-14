"""
XML zu HTML Transformer
Aufgabe 3 - Test Script

Author: Qerim Mehmeti
MN: 42307005
"""
# Mit dem Skript habe ich die XML in eine funktionierende HTML transformiert, damit man die Version auch im Browser sehen kann
try:
    from lxml import etree


    def transform_xml_to_html():
        """
        Transformiert filme.xml mit filme_stylesheet.xsl zu HTML
        """
        print("=== XML zu HTML Transformation ===")

        try:
            # Lade XML-Datei
            with open('filme.xml', 'r', encoding='utf-8') as f:
                xml_content = f.read()

            # Lade XSLT-Stylesheet
            with open('filme_stylesheet.xsl', 'r', encoding='utf-8') as f:
                xsl_content = f.read()

            # Parse XML und XSL
            xml_doc = etree.fromstring(xml_content.encode('utf-8'))
            xsl_doc = etree.fromstring(xsl_content.encode('utf-8'))

            # Erstelle XSLT-Transformer
            transform = etree.XSLT(xsl_doc)

            # Führe Transformation durch
            result = transform(xml_doc)

            # Speichere HTML-Ergebnis
            with open('kino_website.html', 'w', encoding='utf-8') as f:
                f.write(str(result))

            print("SUCCESS: Transformation erfolgreich!")
            print("OUTPUT: HTML-Datei erstellt: kino_website.html")
            print("INFO: Öffne die Datei im Browser um das Ergebnis zu sehen!")

            # Zeige ersten Teil der HTML-Ausgabe
            html_output = str(result)
            print(f"\nErste 500 Zeichen der HTML-Ausgabe:")
            print("-" * 50)
            print(html_output[:500] + "...")

        except FileNotFoundError as e:
            print(f"ERROR: Datei nicht gefunden: {e}")
            print("Stelle sicher, dass filme.xml und filme_stylesheet.xsl im gleichen Ordner sind")

        except Exception as e:
            print(f"ERROR: Fehler bei der Transformation: {e}")


    if __name__ == "__main__":
        transform_xml_to_html()

except ImportError:
    print("ERROR: lxml ist nicht installiert!")
    print("Installiere es mit: pip install lxml")
    print("\nAlternativ teste online: https://www.freeformatter.com/xsl-transformer.html")
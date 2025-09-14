<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<!--
XSLT-Stylesheet für Kinodaten → HTML
Aufgabe 3c - DLBIADPS01-01

Author: Qerim Mehmeti
MN: 42307005

Transformiert XML zu HTML, wie eine Template Engine für APIs
-->

<xsl:template match="/">
    <html>
    <head>
        <title>Kino-Programm</title>
       <style>
            body {
                font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                margin: 0;
                padding: 24px;
                background: #fafafa;
                color: #09090b;
            }
            .header {
                text-align: center;
                margin-bottom: 40px;
                padding: 32px 0;
            }
            .header h1 {
                font-size: 36px;
                font-weight: 700;
                color: #18181b;
                margin: 0 0 8px 0;
            }
            .header p {
                color: #71717a;
                font-size: 18px;
                margin: 0;
            }
            .film-container {
                background: #18181b;
                margin: 24px auto;
                padding: 24px;
                border-radius: 12px;
                box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
                max-width: 800px;
                border: 1px solid #27272a;
            }
            .titel {
                font-size: 28px;
                color: #fafafa;
                font-weight: 600;
                margin-bottom: 12px;
                line-height: 1.2;
            }
            .regisseur {
                font-size: 20px;
                color: #a1a1aa;
                font-weight: 500;
                margin-bottom: 16px;
            }
            .details {
                color: #71717a;
                margin-bottom: 16px;
                font-size: 14px;
                line-height: 1.5;
            }
            .rating {
                background: #09090b;
                color: #fafafa;
                padding: 8px 16px;
                border-radius: 6px;
                display: inline-block;
                margin-top: 8px;
                font-size: 14px;
                font-weight: 500;
                border: 1px solid #27272a;
            }
            .genre { color: #d4d4d8; font-weight: 500; }
            .jahr { color: #a1a1aa; }
            .footer {
                text-align: center;
                margin-top: 48px;
                color: #71717a;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🎬 Kinoprogramm heute</h1>
            <p>Unsere aktuellen Filme</p>
        </div>

        <xsl:for-each select="filme/film">
            <div class="film-container">
                <!-- Titel in großer Schrift (28px) -->
                <div class="titel">
                    <xsl:value-of select="titel"/>
                </div>

                <!-- Regisseur in mittlerer Schrift (20px) -->
                <div class="regisseur">
                    Regie: <xsl:value-of select="regisseur"/>
                </div>

                <!-- Film-Details -->
                <div class="details">
                    <span class="genre">Genre: <xsl:value-of select="genre"/></span> |
                    <span class="jahr">Jahr: <xsl:value-of select="erscheinungsdatum"/></span> |
                    <span>Sprache: <xsl:value-of select="@sprache"/></span>
                </div>

                <!-- Rating mit Hintergrundfarbe -->
                <div class="rating">
                    ⭐ <xsl:value-of select="rating/@wert"/>/10 - <xsl:value-of select="rating"/>
                </div>
            </div>
        </xsl:for-each>

        <div class="footer">
            <p>Generiert mit XSLT • Kino-Website</p>
        </div>
    </body>
    </html>
</xsl:template>

</xsl:stylesheet>
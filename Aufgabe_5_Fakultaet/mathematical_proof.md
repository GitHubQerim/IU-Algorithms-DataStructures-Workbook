# Beweis der Korrektheit durch mathematische Induktion

**Aufgabe 5 - DLBIADPS01-01**  
**Author:** Qerim Mehmeti  
**MN:** 42307005

## Zu beweisende Aussage

**Behauptung P(n):** Die rekursive Implementierung berechnet für alle n ∈ ℕ₀ korrekt n!.

**Definition:** n! = n × (n-1) × (n-2) × ... × 1 für n ≥ 1, und 0! = 1 per Definition.

## Rekursive Implementierung

```python
def factorial_recursive(n):
    if n < 0:
        raise ValueError("Fakultät ist nur für nicht-negative Zahlen definiert")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
```

## Formaler Induktionsbeweis

### Induktionsanfang (Basisfall)

**Zu zeigen:** P(0) und P(1) sind wahr.

**Beweis:**
- **Für n = 0:** `factorial_recursive(0)` gibt `1` zurück. Nach Definition ist 0! = 1.
- **Für n = 1:** `factorial_recursive(1)` gibt `1` zurück. Nach Definition ist 1! = 1.

Der Basisfall ist erfüllt.

### Induktionsvoraussetzung

**Annahme:** Für ein beliebiges k gilt factorial_recursive(k) = k!.

### Induktionsschritt (k → k+1)

**Zu zeigen:** Wenn P(k) wahr ist, dann ist auch P(k+1) wahr.

**Beweis:**

| Ausdruck | Umformung | Begründung |
|----------|-----------|------------|
| factorial_recursive(k+1) | =(k+1)*factorial_recursive(k) | Definition der Funktion |
| | =(k+1)*k! | Induktionsvoraussetzung |
| | =(k+1)! | Definition der Fakultät |

Damit ist P(n) für alle n ∈ ℕ₀ bewiesen.

## Praktische Verifikation

**Testresultate:**

| N | N!(rekursiv) | N!(iterativ) | Übereinstimmung |
|---|--------------|--------------|-----------------|
| 0 | 1 | 1 | Ja |
| 1 | 1 | 1 | Ja |
| 2 | 2 | 2 | Ja |
| 3 | 6 | 6 | Ja |
| 4 | 24 | 24 | Ja |
| 5 | 120 | 120 | Ja |
| 10 | 3628800 | 3628800 | Ja |

## Performance-Vergleich

**Fakultät von 20:**

| Eingabe | Ergebnis | Rekursiv (s) | Iterativ (s) | Faktor |
|---------|----------|--------------|--------------|---------|
| 20 | 2432902008176640000 | 0.00000191s | 0.00000095s | 2.00x langsamer (rekursiv) |

Die rekursive Variante war etwa doppelt so langsam. Grund dafür ist der Overhead durch Funktionsaufrufe und den wachsenden Call-Stack.

## Komplexitätsanalyse

**Zeitkomplexität:** Beide Varianten O(n) – eine Multiplikation pro rekursivem Aufruf bzw. Schleifendurchlauf.

**Speicherkomplexität:** 
- Rekursiv O(n) wegen wachsendem Call-Stack
- Iterativ O(1) konstanter Speicherbedarf

## Fazit

Die rekursive Implementierung spiegelt die mathematische Definition elegant wider und eignet sich gut für Beweise. Die iterative Variante ist praktischer, da sie speicherschonend ist und keine Gefahr eines Stack Overflow birgt. Der Induktionsbeweis garantiert die Korrektheit, während die Performance-Messung die praktischen Unterschiede offenlegt.
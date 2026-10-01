def score(word):
    s = 0.0

    # longueur humaine
    if 6 <= len(word) <= 10:
        s += 0.4

    # présence chiffres
    if any(c.isdigit() for c in word):
        s += 0.3

    # début alphabétique
    if word[:3].isalpha():
        s += 0.2

    # bonus patterns simples
    patterns = ["123", "2024", "love", "pass"]

    if any(p in word.lower() for p in patterns):
        s += 0.3

    return round(s, 2)
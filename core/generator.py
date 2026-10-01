def generate_stream(data):
    texts = data["texts"]
    numbers = data["numbers"]

    # mots simples
    for t in texts:
        yield t

    # combinaison texte + texte
    for t1 in texts:
        for t2 in texts:
            if t1 != t2:
                yield t1 + t2

    # texte + chiffres
    for t in texts:
        for n in numbers:
            yield t + n
            yield n + t
def mutate_stream(word):
    yield word

    mapping = {
        "a": "4",
        "e": "3",
        "i": "1",
        "o": "0",
        "s": "5",
        "l": "1"
    }

    for k, v in mapping.items():
        if k in word:
            yield word.replace(k, v)

    symbols = ["!", "@", "_"]

    for s in symbols:
        yield word + s
        yield s + word
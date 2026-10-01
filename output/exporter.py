def export_stream(word, score_value, file="wordlist.txt"):
    with open(file, "a") as f:
        f.write(f"{word}:{score_value}\n")
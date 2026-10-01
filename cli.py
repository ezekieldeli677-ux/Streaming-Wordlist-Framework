from core.engine import pipeline


def ask(prompt):
    return input(prompt).strip()


def main():
    print("\n=== STREAMING WORDLIST FRAMEWORK ===\n")

    name = ask("First name: ")
    surname = ask("Surname: ")
    year = ask("Birth year: ")
    phone = ask("Phone: ")

    data = {
        "texts": list(filter(None, [name, surname, name + surname])),
        "numbers": list(filter(None, [year, phone[:3] if phone else None, phone[-4:] if phone else None]))
    }

    print("\n[+] Génération en cours...\n")

    pipeline(data, limit=7000)

    print("\n[+] Terminé. Fichier: wordlist.txt")


if __name__ == "__main__":
    main()
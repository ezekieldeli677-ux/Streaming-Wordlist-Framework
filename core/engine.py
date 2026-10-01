from core.generator import generate_stream
from processors.mutations import mutate_stream
from processors.filters import is_valid
from analysis.scoring import score
from output.exporter import export_stream


def pipeline(data, limit=7000):
    """
    Pipeline streaming principal
    """

    count = 0

    for word in generate_stream(data):

        for mutated in mutate_stream(word):

            if not is_valid(mutated):
                continue

            s = score(mutated)

            export_stream(mutated, s)

            count += 1

            if count >= limit:
                print(f"\n[+] Limite atteinte: {limit} mots")
                return
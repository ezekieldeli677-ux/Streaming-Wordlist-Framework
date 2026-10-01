def is_valid(word):
    if len(word) < 4 or len(word) > 16:
        return False

    digit_ratio = sum(c.isdigit() for c in word) / len(word)

    if digit_ratio > 0.7:
        return False

    return True
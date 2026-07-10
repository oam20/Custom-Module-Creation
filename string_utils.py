def reverse_string(text):

    if text is None:
        return None

    revs = text[::-1]
    return revs


def count_words(text):

    if text is None or text.strip() == "":
        return 0

    words = text.split()

    return len(words)


def capitalize_words(text):

    if text is None:
        return None
    
    cap = text.title()

    return cap


def remove_duplicates(text):

    if text is None:
        return None

    result = ""

    for character in text:

        if character not in result:
            result += character

    return result
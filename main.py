def main():
    BOOK_PATH = "books/frankenstein.txt"

    text = get_book_text(BOOK_PATH)
    words = text.split()

    char_count = get_chars_dict(words)
    sorted_chars = get_sorted_chars(char_count)
    report_char_count(sorted_chars, BOOK_PATH)

def get_sorted_chars(char_count):
    """
    Takes in a dict of char -> count pairs and
    Returns an array of char objects sorted by count descending
    """
    chars = []  # array of char objects containing char and its count
    for c in char_count:
        char = {
            "char": c,
            "count": char_count[c]
        }
        chars.append(char)

    # sort the array of chars based on count
    chars.sort(reverse=True, key=lambda char: char["count"])
    return chars

def report_char_count(chars, fname):
    """
    Takes in an array of char objects and
    Prints out a report of char frequencies
    Returns None
    """
    print(f"---------- BEGIN REPORT OF {fname} ----------")
    for char in chars:
        if char["char"].isalpha():
            print(f"The '{char['char']}' character was found {char['count']} times")
        continue
    print(f"---------- END REPORT OF {fname} ----------")
    return


def get_chars_dict(words):
    char_count = {}
    for word in words:
        lowered = word.lower()
        for c in lowered:
            char_count[c] = char_count.get(c, 0) + 1
    return char_count


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
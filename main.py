def main():
    # Book path
    book_path = "books/frankenstein.txt"

    # Get text from the book
    text = get_book_text(book_path)

    # Get the number of words
    num_words = get_num_words(text)

    # Get character dictionary and sorted list
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    # Print report
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    """Return the number of words in the given text."""
    words = text.split()
    return len(words)


def sort_on(d):
    """Return the 'num' value from the dictionary, used for sorting."""
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    """Convert a dictionary of character frequencies to a sorted list."""
    sorted_list = [{"char": ch, "num": num_chars_dict[ch]} for ch in num_chars_dict]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    """Return a dictionary of character frequencies in the given text."""
    chars = {}
    for c in text:
        lowered = c.lower()
        chars[lowered] = chars.get(lowered, 0) + 1
    return chars


def get_book_text(path):
    """Read the content of a book from the given file path."""
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return ""


main()

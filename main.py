def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    char_counts = get_char_count(text)
    print("Character counts:")
    print(char_counts)
    # for char, count in char_counts.items():
    #   print(f"'{char}': {count}")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    char_count = {}  # Initialize an empty dictionary to store character counts
    for char in text:  # Iterate over each character in the text
        char = char.lower()  # Convert character to lowercase for case insensitivity
        if char in char_count:  # If character is already in dictionary
            char_count[char] += 1  # Increment the count by 1
        else:
            char_count[char] = 1  # If character is not in dictionary, add it with count 1
    return char_count  # Return the dictionary with character counts

main()


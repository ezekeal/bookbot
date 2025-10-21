import sys
from stats import get_num_words, get_char_counts, sort_chars

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_uri = sys.argv[1]
    book_text = get_book_text(book_uri)
    char_counts = get_char_counts(book_text)
    sorted_chars = sort_chars(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_uri}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    for c in sorted_chars:
        print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")

main()
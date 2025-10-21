def get_num_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def get_char_counts(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_chars(char_counts):
    char_list = []
    for c in char_counts:
        if c.isalpha():
            char_list.append({"char": c, "num": char_counts[c]})
    char_list.sort(reverse=True, key=lambda x: x["num"])
    return char_list
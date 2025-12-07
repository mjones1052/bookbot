def word_count(book_text):
    return book_text.split()

def char_count(book_text):
    char_count = {}
    book_text_lower = book_text.lower()
    for char in book_text_lower:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_chars(char_count):
    sorted_chars = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    return [{char: count} for char, count in sorted_chars.items()]

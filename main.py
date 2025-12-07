import sys

if sys.argv and len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

from stats import char_count
from stats import word_count
from stats import sort_chars

def main():
	filepath = sys.argv[1]
	book_text = get_book_text(filepath)
	words = len(word_count(book_text))
	print_text = f"Found {words} total words"
	#print(sort_chars(char_count(book_text)))
	#print(print_text,char_count(book_text))
	print("============ BOOKBOT ============")
	print("Analyzing book found at", filepath)
	print("----------- Word Count ----------")
	print(print_text)
	print("--------- Character Count -------")
	for char_dict in sort_chars(char_count(book_text)):
		char, count = list(char_dict.items())[0]
		print(f"{char}: {count}")
	print("============= END ===============")
main()


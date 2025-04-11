from stats import get_num_words, get_num_str, order_data
import sys

def get_book_text(filepath):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    print(f'Found {num_words} total words')
    str_dic = get_num_str(text)
    order_data(str_dic)

main()
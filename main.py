from stats import get_book_text, get_char_counts,format_report
import sys


def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = args[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(get_book_text(file_path))
    print("--------- Character Count -------")
    format_report(file_path)
    print("============= END ===============")
    
main()
    
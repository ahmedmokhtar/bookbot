from stats import get_num_words, count_chars, sort_dict
import sys

def get_book_text(fpath):
  with open(fpath) as f:
    content = f.read()
  return content


def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  fpath = sys.argv[1]
  content = get_book_text(fpath)
  num_char = count_chars(content) # a dict of letters and their count
  num_words = get_num_words(content)
  print("\n============ BOOKBOT ============\n")
  print(f"Analyzing book found at {fpath}\n")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words\n")
  print("--------- Character Count -------")
  sorted_dict = sort_dict(num_char)
  for dict in sorted_dict:
    if dict["char"].isalpha():
      print(f"{dict["char"]}: {dict["num"]}")

main()
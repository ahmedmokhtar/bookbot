def get_num_words(text):
  words = text.split()
  return len(words)

def count_chars(text):
  lower_text = text.lower()
  chars = list(lower_text)
  char_count = {}
  for char in chars:
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1
  return char_count

def sort_dict(dict):
  dict_list = []
  for key in dict:
    dict_list.append({"char": key, "num": dict[key]})
    dict_list.sort(reverse=True, key=sort_on)
  return dict_list
  
def sort_on(dict):
  return dict["num"]
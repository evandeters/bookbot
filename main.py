def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    print(num_words)
    print()
    lc = count_letters(text)
    lc = dict_to_list(lc)
    lc.sort(reverse=True, key=sort_on)
    for letter in lc:
        print(f"The \'{letter['letter']}\' character was found {letter['num']} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_letters(text):
    text = text.lower()
    letters = {}
    for c in text:
        if not c.isalpha():
            continue
        if c not in letters:
            letters[c] = 1
        else:
            letters[c] += 1
    return letters


def dict_to_list(dict):
    char_list = []
    for key in dict:
        char_list.append({'letter': key, 'num': dict[key]})
    return char_list


def sort_on(dict):
    return dict["num"]


main()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document \n")
    get_characthers_in_string(text.lower())


def get_characthers_in_string(text):
    characters = {}
    for character in text:
        if character.isalpha():
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1

    sorted_characters = dict(sorted( characters.items(), key=lambda x:x[0] ) )
    for character_to_show in sorted_characters:
        print(f"The {character_to_show} character was found {characters[character_to_show]} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

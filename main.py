def main() :
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_count = get_words_count(text)
    characters_count = get_characters_count(text)
    characters_by_frequency_desc = get_characters_by_frequency_desc(characters_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the document")
    print()
    for c in characters_by_frequency_desc:
        print(f"The '{(c['character'])}' character was found {(c['num'])} times")
    print("--- End report ---")
   


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words_count(fulltext):
    words = fulltext.split()
    return len(words)

def get_characters_count(fulltext):
    count = {}
    lowered_text = fulltext.lower()
    characters = list(lowered_text)
    for c in characters:
        if c in count :
            count[c] += 1
        else:
            count[c] = 1
    return count

def sort_on(count):
    return count["num"]

def get_characters_by_frequency_desc (count):
    count_in_order = []
    for c in count :
        if c.isalpha() == True:
            count_in_order.append({"character" : c , "num" : count[c]})
            count_in_order.sort(reverse=True, key=sort_on)
    return count_in_order 






def characters_report(count):
    for c in count:
        return (f"The {c} character was found {characters_count[c]} times") 
           

main ()



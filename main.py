def main() :
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = countwords(text)
    count_characters = countcharacters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words} words found in the document")
    print()
    list_in_order = put_in_order(count_characters)
    for l in list_in_order:
        print(f"The '{(l['character'])}' character was found {(l['num'])} times")
    print("--- End report ---")
   


def get_book_text(path):
    with open(path) as f:
        return f.read()

def countwords(fulltext):
    words = fulltext.split()
    return len(words)

def countcharacters(fulltext):
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

def put_in_order (count):
    count_in_order = []
    for c in count :
        if c.isalpha() == True:
            count_in_order.append({"character" : c , "num" : count[c]})
            count_in_order.sort(reverse=True, key=sort_on)
    return count_in_order 






def characters_report(count):
    for c in count:
        return (f"The {c} character was found {count_characters[c]} times") 
           

main ()



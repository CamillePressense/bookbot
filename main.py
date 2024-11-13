def main() :
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = countwords(text)
    print(count_words)

    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def countwords(fulltext):
    words = fulltext.split()
    return len(words)
    

main ()



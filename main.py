import sys
if len(sys.argv)!=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]
def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text
def sort_on(c):
    return c["num"]


def main(path) :
    print("========= BOOKBOT =========")
    print(f"Analyzing book found at {path}...")
    print("--------- World Count ---------")    
    l={}
    tx = get_book_text(path)
    from stats import get_words
    from stats import get_num_letters
    c = get_num_letters(tx)       
    l=dict(sorted(c.items(), key=lambda item:item[1], reverse = True))
    wc = get_words(tx)
    print(f"Found {wc} total words ")
    print("--------- Character Count ---------")
    for char, num in l.items():
        if char.isalpha() == True:
            print(f"{char}: {num}")
        
main(path)
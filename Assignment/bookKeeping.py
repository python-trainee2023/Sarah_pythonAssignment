author = input("What Author would you like to look for? : ")
try:
    with open("book.txt", "r") as record:
        listing = record.readlines()
        books = []
        for item in listing:
            if item.find(author) != -1:
                # print("Author Found!!")
                row = listing.index(item)
                books.append(listing[row])
                # print(listing[row])
        if not books:
            print("No books found by the Author ", author)
        else:
            print("Author Found")
            for book in books:
                print(book)
except FileNotFoundError:
    print("The 'book.txt' file does not exist.")
finally:
    record.close()

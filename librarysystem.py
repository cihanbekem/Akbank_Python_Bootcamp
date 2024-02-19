#CİHAN BEKEM Library Management System cihanbekemcb@gmail.com
class Library:
    #'books.txt'dosyasını açar
    def __init__(self):
        self.file = open("books.txt", "a+")

    #dosyayı kapatır
    def __del__(self):
        self.file.close()

    def list_books(self):
        #dosyanın başına gider
        self.file.seek(0)
        #tüm kitapları okuyup listeye kaydeder
        books = self.file.readlines()
        if not books:
            print("There aren't any books found.")
        else:
            for book in books:
                #kitap bilgilerini yazdırır
                book_info = book.strip().split(',')
                print("- Book Name:", book_info[0])
                print("- Author:", book_info[1])
                print("- Release Date:", book_info[2])
                print("- Number of Pages:", book_info[3])
                print()

    def add_book(self):
        #yeni kitap eklemek için bilgi alır
        book_title = input("Please enter the book title: ")
        book_author = input("Please enter the book author: ")
        release_date = input("Please enter the release date: ")
        num_pages = input("Please enter the number of pages: ")
        #yeni kitap için bilgi alır
        book_info = f"{book_title},{book_author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print("Book has been added successfully!")
        #toplam kitap sayısını günceller
        self.update_total_books()

    def remove_book(self):
        book_title = input("Please enter the title of the book to remove: ")
        self.file.seek(0)  # Dosyanın başına gider
        books = self.file.readlines()
        updated_books = [book for book in books if book.split(',')[0] != book_title]
        self.file.seek(0)  # Dosyanın başına döner
        #dosyadaki kitapları temizler
        self.file.truncate(0)
        #kitap sayısını yazar
        self.file.writelines(updated_books)
        print("Book has been removed successfully!")
        self.update_total_books()

    def update_total_books(self):
        self.file.seek(0)
        total_books = sum(1 for _ in self.file)
        print("Total number of books:", total_books)


lib = Library()

while True:
    #menü oluşturur
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Press 'q' For Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "q":
        break
    else:
        print("Invalid choice. Please enter a valid option.")

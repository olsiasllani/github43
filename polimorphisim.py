# Klasë e përgjithshme (Base class)
class Book:
    def display_info(self):
        raise NotImplementedError("Subclasses must implement this method")

# Klasë e trashëguar (Derived class) - Librat me tekst
class TextBook(Book):
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        return f"TextBook: {self.title} by {self.author}, {self.pages} pages."

# Klasë e trashëguar (Derived class) - Librat me audio
class AudioBook(Book):
    def __init__(self, title, author, duration):
        self.title = title
        self.author = author
        self.duration = duration

    def display_info(self):
        return f"AudioBook: {self.title} by {self.author}, Duration: {self.duration} hours."

# Funksion që pranon një libër dhe shfaq informacionin përkatës
def show_book_info(book):
    print(book.display_info())

# Krijo disa libra
book1 = TextBook("Python Programming", "John Doe", 350)
book2 = AudioBook("Learning AI", "Jane Smith", 12)

# Përdor polimorfizmin për të shfaqur informacionin
show_book_info(book1)  # Do të thërrasë metodën "display_info" të klasës TextBook
show_book_info(book2)  # Do të thërrasë metodën "display_info" të klasës AudioBook

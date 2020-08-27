import csv
from application import db
from orm.models import Book


def import_csv():
    with open("books.csv") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip the headers

        for isbn, title, author, year in reader:
            book = Book(isbn=isbn, title=title, author=author, year=year)
            try:
                db.session.add(book)
                db.session.commit()
            except:
                print(f'{book.isbn}--{book.title} is already in database.')


if __name__ == "__main__":
    import_csv()

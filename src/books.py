import csv
from tqdm import tqdm
from app import db
from orm.models import *


def insert_csv_to_db():
    with open("books.csv") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip the headers

        for isbn, title, author, year in tqdm(reader, desc='Insert books data to database'):
            book = Book(isbn=isbn, title=title, author=author, year=year)
            try:
                db.session.add(book)
                db.session.commit()
            except:
                print(f'{book.isbn}--{book.title} is already in database.')
        print('Import books data completed!')


if __name__ == '__main__':
    db.create_all()
    insert_csv_to_db()

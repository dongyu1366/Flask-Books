import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


# connect to the database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# import csv data and insert to database
def import_csv():
    f = open("books.csv")
    reader = csv.reader(f)
    next(reader, None)  # skip the headers

    for isbn, title, author, year in reader:
        try:
            db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                        {"isbn":isbn, "title":title, "author":author, "year":year})
        except:
            pass
        db.commit()


if __name__ == "__main__":
    import_csv()


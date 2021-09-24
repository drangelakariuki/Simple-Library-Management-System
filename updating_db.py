# Module that conducts database transactions. If a book is borrowed, the database is updated and if it is
# is added to database
import psycopg2
from datetime import timedelta, date
from book_loan import loan_book


def update_db():
    conn = psycopg2.connect(database='Library', user='postgres', password='kui', host='localhost', port=5432)
    with conn.cursor() as cur:
        # find available copies with that specific isbn
        cur.execute("Select distinct copies from book_details where book_id = '978-1-5098-0033-9' ")
        available_copies = int(cur.fetchone()[0])
        print(available_copies)

        # find number of copies loaned out with that specific isbn
        cur.execute("Select loaned from loans where book_id = '978-1-5098-0033-9' ")
        loaned = int(cur.fetchone()[0])
        print(loaned)

        # reduce number of books by loaned copies
        remaining_copies = available_copies - loaned
        remaining_copies1 = str(remaining_copies)
        print(remaining_copies)
        query = "Update book_details set copies = %s where book_id = '978-1-5098-0033-9'"
        cur.execute(query, (remaining_copies1,))



update_db()

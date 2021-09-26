import psycopg2
from datetime import timedelta, date


def return_book():
    book_id = input("Please enter the ISBN of book to return: ")
    return_date = date.today()
    loaned = 1
    conn = psycopg2.connect(database='Library', user='postgres', password='kui', host='localhost', port=5432)
    cur = conn.cursor()
    with conn:
        # fetch copies in system
        cur.execute(("Select distinct copies from book_details where book_id = '%s' " % book_id))
        available_copies = int(cur.fetchone()[0])
        # increase number of copies in the system
        updated_copies = available_copies + loaned
        updated_copies1 = str(updated_copies)
        # return query
        cur.execute("UPDATE book_details set copies = %s where book_id = '%s' " % (updated_copies1, book_id))
        conn.commit()
        print(cur.rowcount)
    if cur.rowcount > 0:

        print("Book returned, book_id {}".format(book_id))

    cur.close
    conn.close


if __name__ == '__main__':
    return_book()





# A module that creates loaned book table, (for borrowing books)
from datetime import timedelta, date
import psycopg2


def loan_book():
    conn = psycopg2.connect(database='Library', user='postgres', password='kui', host='localhost', port=5432)
    cur = conn.cursor()
    loaned = '1'
    loan_date = date.today()
    due_back = loan_date + timedelta(days=14)
    # fetch available copies of the book. Borrowing is successful if the available copies are more than one.
    isbn = input("Please enter the ISBN of book you want to loan: ")
    search_query = "Select distinct copies from book_details where book_id = '%s' " % isbn
    cur.execute(search_query)
    available_copies = int(cur.fetchone()[0])
    print(available_copies, 'copies of the book are available.')
    if available_copies >= 1:
        info = input("Please enter the loan details at the prompts or type exit at any time to "
                     "exit the program. Press enter to continue: ")
        loop = 'yes'
        while True and loop == 'yes':
            loan_id = input('Enter the loan ID(random 4 numbers): ')
            if loan_id == 'exit':
                loop = 'no'
                break
            else:
                while loan_id:
                    user_id = input('Enter the student admission unique ID: ')
                    if user_id == 'exit':
                        loop = 'no'
                        break
                    else:
                        while user_id:
                            book_id = input("Please enter the ISBN: ")
                            if book_id == 'exit':
                                loop = 'no'
                                break
                            else:
                                loop = 'no'
                                with conn:
                                    # borrow book
                                    cur.execute("""INSERT INTO loans (loan_id, user_id, book_id, loaned,
                                                loan_date,due_back)VALUES(%s,%s,%s,%s,%s,%s)""",
                                                (loan_id, user_id, book_id, loaned, loan_date, due_back))
                                    print("New loan has been added")
                                    # updating the database, reduce the number of copies.
                                    remaining_copies = available_copies - int(loaned)
                                    remaining_copies1 = str(remaining_copies)
                                    query = " Update book_details set copies = %s where book_id = '%s'" % \
                                            (remaining_copies1, isbn)
                                    cur.execute(query)
                                    print('Database updated.')
                                conn.commit()
                                cur.close
                                conn.close
                                return

    elif available_copies == 0:
        print('Book unavailable at the moment. Try to borrow another book.')


if __name__ == '__main__':
    loan_book()

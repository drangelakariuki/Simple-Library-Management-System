# A module that creates loaned book table.
from datetime import timedelta, date
import psycopg2


def loan_book():
    conn = psycopg2.connect(database='Library', user='postgres', password='kui', host='localhost', port=5432)
    cur = conn.cursor()
    loaned = '1'
    loan_date = date.today()
    due_back = loan_date + timedelta(days=14)

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
                                cur.execute("""INSERT INTO loans (loan_id, user_id, book_id, loaned,
                                            loan_date,due_back)VALUES(%s,%s,%s,%s,%s,%s)""",
                                            (loan_id, user_id, book_id, loaned, loan_date, due_back))

                                conn.commit()
                                print("New loan has been added")
                                return


if __name__ == '__main__':
    loan_book()

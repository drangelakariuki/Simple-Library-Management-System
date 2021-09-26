import psycopg2
from datetime import date

conn = psycopg2.connect(database='Library', user='postgres', password='kui', host='localhost', port=5432)
cur = conn.cursor()


def add_book():
    info = input("Please enter the book details at the prompts or type exit at any time to "
                 "exit the program. Press enter to continue: ")
    loop = 'yes'
    while True and loop == 'yes':
        book_id = input("Please enter the ISBN: ")
        if book_id == 'exit':
            break
        else:
            while book_id:
                book_name = input("Please enter the book name: ")
                if book_name == 'exit':
                    loop = 'no'
                    break
                else:
                    while book_name:
                        book_author = input("Please enter the book author: ")
                        if book_author == 'exit':
                            loop = 'no'
                            break
                        else:
                            while book_author:
                                price = input('Enter cost of borrowing book(Kshs): ')
                                if price == 'exit':
                                    loop = 'no'
                                    break
                                else:
                                    while price:
                                        copies = input('Enter the number of copies available: ')
                                        while copies:
                                            if copies == 'exit':
                                                loop = 'no'
                                                return
                                            else:
                                                loop = 'no'
                                                with conn:
                                                    cur.execute("""INSERT into book_details (book_id, book_name,
                                                            book_author, price,copies) VALUES(%s,%s,%s,%s,%s)""",
                                                            (book_id, book_name, book_author, price, copies))

                                                conn.commit()
                                                print("New book has been added")
                                                return
                                            cur.close
                                            conn.close


if __name__ == '__main__':
    add_book()
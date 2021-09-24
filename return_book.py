import psycopg2
from datetime import timedelta, date


def return_book():
    book_id = input("Please enter the ISBN of book to return: ")
    return_date = date.today()
    loaned = '1'
    conn = psycopg2.connect(database='Library', user='postgres', password='kui', host='localhost', port=5432)
    cur = conn.cursor()
    with conn:
        return_query = ("UPDATE book_details set copies = %s where book_id =  '978-1-5098-0033-9' ")




# A program to create the postgresql database.

import psycopg2


def db_setup():
    conn = psycopg2.connect(database='Library', user='postgres', password='kui', host='localhost', port=5432)
    with conn.cursor() as cur:
        # create table
        cur.execute("""CREATE TABLE IF NOT EXISTS book_details (
    book_id varchar PRIMARY KEY NOT NULL,
    book_name varchar NOT NULL,
    book_author varchar NOT NULL,
    price int NOT NULL,
    copies int NOT NULL);""")
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
      user_id int primary key NOT NULL,
      first_name varchar,
      last_name varchar,
      email varchar);""")
        cur.execute("""CREATE TABLE IF NOT EXISTS loans(
    loan_id integer PRIMARY KEY NOT NULL,
    user_id int,
    book_id varchar,
    loaned int,
    loan_date date,
    due_back date);""")
    print("Tables created successfully in PostgreSQL ")
    # close communication with the PostgreSQL database server
    cur.close()
    # commit the changes
    conn.commit()
    # close database connection
    conn.close()


if __name__ == '__main__':
    db_setup()

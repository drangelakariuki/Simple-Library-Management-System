# A module to search users.
from datetime import date
import psycopg2
try:
    conn = psycopg2.connect(database='Library', user='postgres', password='kui', host='localhost', port=5432)
    with conn.cursor() as cur:
        cur.execute('Select * from Users')
        user_records = cur.fetchall()
        print('Print each row and its columns values')
        for row in user_records:
            print('User_ID =', row[0])
            print('first_name =', row[1])
            print('last_name=', row[2])
            print('email =', row[3], '\n')


except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if conn:
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")
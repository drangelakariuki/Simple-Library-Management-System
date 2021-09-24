# A module to add user to the database
import psycopg2
from datetime import date


def user_add():
    conn = psycopg2.connect(database='Library', user='postgres', password='kui', host='localhost', port=5432)
    cur = conn.cursor()
    info = input("Please enter the library user details at the prompts or type exit at any time to "
                 "exit the program. Press enter to continue: ")
    loop = 'yes'
    while True and loop == 'yes':
        user_id = input('Enter the student admission unique ID: ')
        if user_id == 'exit':
            loop = 'no'
            break
        else:
            while user_id:
                first_name = input('Enter the first name: ')
                if first_name == 'exit':
                    loop = 'no'
                    break
                else:
                    while first_name:
                        last_name = input('Enter the last name: ')
                        if last_name == 'exit':
                            loop = 'no'
                            break
                        else:
                            while last_name:
                                email = input('Enter the email address: ')
                                if email == 'exit':
                                    loop = 'no'
                                    return
                                else:
                                    loop = 'no'
                                    with conn:
                                        cur.execute("""INSERT into users (user_id, first_name, last_name, email) 
                                        VALUES(%s,%s,%s,%s)""", (user_id, first_name, last_name, email))

                                    conn.commit()
                                    print("New user has been added")
                                    return


if __name__ == '__main__':
    user_add()

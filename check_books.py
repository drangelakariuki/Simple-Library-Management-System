import psycopg2

# A module to search books by author name, book name and check if a copy is available.

conn = psycopg2.connect(database='Library', user='postgres', password='kui', host='localhost', port=5432)


def check_all():
    with conn.cursor() as cur:
        cur.execute('Select * from book_details')
        book_records = cur.fetchall()
        for row in book_records:
            print('Book_ID =', row[0])
            print('Book_Name =', row[1])
            print('Book_Author=', row[2])
            print('Price =', row[3])
            print('Copies =', row[4], '\n')


def author_name():
    with conn.cursor() as cur:
        cur.execute("Select distinct book_author from book_details")
        author_records = cur.fetchall()
        for row in author_records:
            print(row[0])


def book_names():
    with conn.cursor() as cur:
        cur.execute("Select distinct book_name from book_details")
        name_records = cur.fetchall()
        for row in name_records:
            print(row[0])


def available_copies():
    with conn.cursor() as cur:
        cur.execute("Select book_name from book_details where copies >= 0")
        copies_available = cur.fetchall()
        for row in copies_available:
            print(row[0])


def selection_calls():
    valid_selections = ('1', '2', '3', '4')
    message = input("Welcome to the main menu. Press enter to continue: ")
    loop = 'yes'
    while True and loop == 'yes':
        selection = input("Enter 1, 2, 3, or 4. (Type exit to exit program)\n"
                          "1 - Check all books available in the library\n"
                          "2 - Check by  Author's Available\n"
                          "3 - Check by Full Book Name\n"
                          "4 - Check Available Books\n")
        if selection == 'exit':
            break
        else:
            if selection in valid_selections:
                loop = 'no'

            else:
                print('\nValue: {} did not match any menu choice'.format(selection))
                loop = 'yes'
    return selection


def checking_book():
    selection = selection_calls()
    if selection == '1':
        check_all()
    elif selection == '2':
        author_name()
    elif selection == '3':
        book_names()
    elif selection == '4':
        available_copies()


if __name__ == '__main__':
    checking_book()







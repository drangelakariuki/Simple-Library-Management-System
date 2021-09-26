import psycopg2
from datetime import timedelta, date
from books_add import add_book
from user_add import user_add
from check_books import checking_book
from checking_user import checking_user
from book_loan import loan_book
from return_book import return_book


def menu_selection():
    valid_selections = ('1', '2', '3', '4', '5', '6')
    message = input("Welcome to the main menu. Press enter to continue: ")
    loop = 'yes'
    while True and loop == 'yes':
        selection = input("\nPlease select from the following menu (Type exit to exit program) \n"
                          "To check all books enter 1 \n"
                          "To check all users enter 2 \n"
                          "To add a user enter 3 \n"
                          "To add a book enter 4 \n"
                          "To borrow book enter 5 \n"
                          "To return book enter 6 \n"
                          "\nEnter choice: ")
        if selection == 'exit':
            break
        else:
            if selection in valid_selections:
                loop = 'no'

            else:
                print('\nValue: {} did not match any menu choice'.format(selection))
                loop = 'yes'
    return selection


def selection_calls():
    selection = menu_selection()

    if selection == '1':
        checking_book()

    elif selection == '2':
        checking_user()

    elif selection == '3':
        user_add()

    elif selection == '4':
        add_book()

    elif selection == '5':
        loan_book()

    elif selection == '6':
        return_book()


if __name__ == '__main__':
    selection_calls()
    # ask admin if they want to do something else
    do_more = input('Would you like to do anything else? Type yes or no.')
    if do_more.lower() == 'no':
        print('Welcome again!')
    if do_more.lower() == 'yes':
        selection_calls()


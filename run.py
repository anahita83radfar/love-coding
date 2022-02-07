def get_user_data():
    """
    Get figures input from the user.
    We run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of one of the listed numbers.
    The loop will repeatedly request data until it is valid.
    """
    print('*** Welcome to Love Coding Survey Data Analysis ***')
    print('Please enter one of the listed numbers to see the answer.\n')
    print('1.What percentage of women and men are developers?')
    print('Enter "1" to see the answer\n')
    print('2.Which are the five most common programming languages?')
    print('Enter "2" to see the answer\n')
    print('3.Which are the five most common languages among developers types?')
    print('Enter "3" to see the answer\n')
    print('Enter "0" to exit\n')

    while True:

        data = input("Enter here:\n")

        if data not in ["0", "1", "2", "3"]:
            print("Invalid data, Please try again.")
        else:
            if data == "1":
                print("Answer 1")
            elif data == "2":
                print("Answer 2")
            elif data == "3":
                print("Answer 3")
            elif data == "0":
                break


get_user_data()

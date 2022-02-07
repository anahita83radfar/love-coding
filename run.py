import csv
from collections import Counter


def get_user_data():
    """
    Get figures input from the user.
    We run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of one of the listed numbers.
    The loop will repeatedly request data until it is valid.
    """
    gender = gender_analyse()
    languages = common_language()
    developers = developer_types()

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
                print(gender)
            elif data == "2":
                print(languages)
            elif data == "3":
                print(developers)
            elif data == "0":
                break


def gender_analyse():
    """
    Load in CSV file, open it, and read it.
    Run a for loop to access "Gender" column data and count man and woman
    answers. Calculate that information to see what percentage of people
    answered this developer survey are males and what percentage are females.
    """
    with open('survey_results_public.csv') as file:
        csv_reader = csv.DictReader(file)

        man_count = 0
        woman_count = 0

        for line in csv_reader:
            if line['Gender'] == 'Man':
                man_count += 1
            elif line['Gender'] == 'Woman':
                woman_count += 1

    total = man_count + woman_count

    man_percent = (man_count / total) * 100
    man_percent = round(man_percent)

    woman_percent = (woman_count / total) * 100
    woman_percent = round(woman_percent)

    gender = f'Man: {man_percent}%\nWoman: {woman_percent}%'

    return gender


def common_language():
    """
    Load in CSV file, open it, and read it.
    Run a for loop to access "LanguageHaveWorkedWith" column
    data and count languages. Run a for loop to see the five
    most common languages developers currently working with
    and calculate the percentage for each one of these languages.
    """
    with open('survey_results_public.csv') as file:
        csv_reader = csv.DictReader(file)
        total = 0

        language_counter = Counter()

        for line in csv_reader:
            languages = line['LanguageHaveWorkedWith'].split(';')

            language_counter.update(languages)

            total += 1
    output = ""
    for key, value in language_counter.most_common(5):
        language_percent = (value / total) * 100
        language_percent = round(language_percent)
        output = output + f'{key}: {language_percent}%\n'

    return output


def developer_types():
    """
    Load in CSV file, open it, and read it.
    Run a for loop to access "DevType" column data and loop over that
    information to access all of the developer's types. Run a for loop
    to see the five most common languages that specific developer type
    working with and calculate the percentage for each one of these languages.
    """
    with open('survey_results_public.csv') as file:
        csv_reader = csv.DictReader(file)

        dev_type_info = {}
        for line in csv_reader:
            dev_types = line['DevType'].split(";")
            for dev_type in dev_types:
                dev_type_info.setdefault(dev_type, {
                    'total': 0,
                    'language_counter': Counter()
                })
                languages = line['LanguageHaveWorkedWith'].split(";")
                dev_type_info[dev_type]['language_counter'].update(languages)
                dev_type_info[dev_type]['total'] += 1
    output = ""
    for dev_type, info in dev_type_info.items():
        output = output + "\n" + dev_type
        for language, value in info['language_counter'].most_common(5):
            language_percent = (value / info['total']) * 100
            language_percent = round(language_percent)
            developers = f'\t{language}: {language_percent}%'

            output = output + "\n" + developers
    return output


get_user_data()

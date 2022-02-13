# Love Coding

Love coding is a Python terminal application, which runs in the Code Institute mock terminal on Heroku.
The application makes it possible that the user to glean insights from the 2021 Stack Overflow Developer Survey results.
The application goal is that the user can be able to pull out the information that she/he is looking for from an inputted dataset.

[Here is the live version of my project](https://love-coding.herokuapp.com/)

![Responsive page](/images/responsive.jpg)

# How to use

In this application, the user is going to receive a list of questions by running the application. The answer to each question is the result of parsing and analyzing the data of a specific part from the 2021 Stack Overflow Developer Survey results.  By entering one of the listed numbers below and after the questions, the user can see the answer or result of data analysis and also exit from the application.

# Features
## Existing Features
- ### Accepts user input

![Accepts user input](/images/input.jpg)

- ### Input validation and error-checking
  - User must enter one of the listed numbers
  - User cannot enter any number other than the listed numbers
  - User cannot enter any letters or symbols

![Input validation and error-checking](/images/invalid.jpg)

## Future Features
- Allow user to save results of data analysis to another file

# Data Model
   This program needs to get data from the user and check if the data is provided valid. With entering invalid data, the user receives an error message on the terminal. It will repeatedly request data from the user until it is valid. If the data is provided valid, this program going to get survey data from the CSV file, parse and calculate information out of the data, add results to another CSV file, and print results to the terminal.

   ![Diagram](/images/diagram.jpg)

   I decided to use several different functions as my model. The first function `get_user_data()`, get figures input from the user to collect a valid string of data from the user via the terminal, which must be a string of one of the listed numbers. It will repeatedly request data, until it is valid and print out the result by the print method. 
   
   The second function `gender_analyse()`, the third function `common_language()`, and the fourth function `developer_types()`, load in CSV file, get a specific column data such as "Gender", "LanguageHaveWorkedWith" and "DevType" from the "survey_results_public.csv" file and parse that information out of the data. These functions count and calculate that information so that to see, what percentage of people who answered this developer survey are male and what percentage is female, which are the five most common languages developers currently working with and which are the most common languages among developers types. 
   
   The last function some take three parameters `save_data(gender, languages, developers)`, create another CSV file, "survey_results_analyse.csv" to save results of data analysis from return of the second, third and fourth function. This function by creating rows in the new file makes it possible to make a header and put the output of previous functions,` gender`, `languages`, and `developers` in each row.

# Testing

I have manually tested this project by doing the following:

- Passed the code through a PEP8 linter and confirmed there are no problems

- Given invalid inputs: numbers other than numbers are considered, letters and symbols

- Tested in my local terminal and the Code Institute Heroku terminal

### Bugs
#### Solved Bugs
- I was getting EOFerror because of an `input()` function in my project.


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

- I handled this exception by adding `try` and `except` keywords.

      while True:
          try:
              data = input("Enter here:\n")

              if data not in ["0", "1", "2", "3"]:
                  print("Invalid data, Please try again.")
                  continue
          except EOFError:
              print("Invalid data, Please try again.")
              continue
          else:
              if data == "1":
                  print(gender)
              elif data == "2":
                  print(languages)
              elif data == "3":
                  print(developers)
              elif data == "0":
                  break


#### Remaining Bugs
- No bugs remaining

### Validator testing
- PEP8
   - No errors were returned from PEP8online.com

# Deployment
This project was deployed using Code Institute's mock terminal for Heroku.
- Steps for deployment:
  - Fork or clone this repository
  - Create a new Heroku app
  - Set the buildbacks to `Python` and `NodeJS` in that order
  - Link the Heroku app to the repository
  - Click on **Deploy**

# Credits
### Content
- Code Institute for the deployment terminal
- I had taken data from [Stack Overflow Annual Developer Survey](https://insights.stackoverflow.com/survey) to analyze the 2021 Stack Overflow Developer Survey
- The application idea is taken from [Specific YouTube Tutorial](https://www.youtube.com/watch?v=_P7X8tMplsw&t=1044s)
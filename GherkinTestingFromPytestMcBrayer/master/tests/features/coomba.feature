import pytest-bdd import scenario, given, when, then
import pytest
Feature:CucumberBasket
     As an application user, I want to enter my information into the fields and have desired results come out on the other end.
Scenario: Customer wants to calculate retirement age info at specific date
          Given a users birth year is above 1959
          When their birth year is entered
          Then program returns 67 for retirement age and no error tags
  Scenario: Customer wants to calculate retirement age info if born under 1937
          Given a users birth year is less than 1937
          When their birth year is entered
          Then program returns 65 for retirement age and no error tags
#good two above

  Scenario: Customer enters birth information
          Given a users age month and birth month info are 1956, 4 ,65 ,9
          When their information is entered > 12 and entered into calculator
          Then the retirement year output is 2022 and 1
#3 above done
  Scenario: Customer enters their birth information
          Given a user is entering their birth year information as 1956, 4, 65, 8
          When the birth month plus age month are <=12 and entered into calculator
          Then the retirement year output is 2022 and 1
#4 above done
  Scenario: Customer enters birth and age information
          Given a user has a birth year below 1900
#          When the birth year is entered into the calculator
          Then pyTest raises ValueError
#5 above

  Scenario: Customer enters birth and age information
          Given a user has a birth year of 2021+
          Then  pyTest raises ValueError
    #6 above
  Scenario: A user is entering birth and age information
          Given a user's birth month is <1
#          When that month is entered into the calculator
          Then ppyTest raises ValueError
    #7 above
  Scenario: A user is entering birth and age information
          Given a user's birth month is >12
#          When that month is entered into the calculator
          Then pyTest raises ValueError
    #8 above
  Scenario: A user is entering birth and age information
          Given a user's birth age year is >67
#          When that month is entered into the calculator
          Then pyTest raises ValueError
    #9 above
    Scenario: A user is entering birth and age information
          Given a user's birth age year is <65
#          When that month is entered into the calculator
          Then pyTest raises ValueError
      #10 above
  #Scenario Outline: year ranges
     Scenario Outline: Entering range of dates
          Given customer enters multiple dates
          When user's <year> entered between 1937-1943
          Then the retirement age is: <age>
  Examples:
    | year | age |
    | 1937 | 65  |
    | 1938 | 65  |
    | 1939 | 65  |
    | 1940 | 65  |
    | 1941 | 65  |
    | 1942 | 65  |
    | 1943 | 65  |

    #11 above
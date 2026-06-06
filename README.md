# Driving-License-validity-calculator
Python project that calculates driving licence eligibility and expiry date based on age and date of birth.
# Driving License Validity Calculator

A beginner Python project that calculates driving licence eligibility and expiry dates based on a user's date of birth.

## Features

* Takes user name and date of birth as input
* Calculates the user's current age
* Checks driving licence eligibility
* Provides special eligibility information for users aged 16–17 years
* Calculates licence expiry dates according to the implemented rules

## Eligibility Rules

* Below 16 years: Not eligible for a driving licence
* 16–17 years: Eligible for a gearless two-wheeler licence
* 18–29 years: Licence valid until age 40
* 30–49 years: Licence valid for 10 years
* 50–54 years: Licence valid until age 60
* 55 years and above: Licence valid for 5 years

## Technologies Used

* Python
* datetime module

## How to Run

1. Download or clone the repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

## Sample Output

```text
----- Driving Licence Details -----

Name: Rahul
Age: 25
Licence Expiry Date: 15-08-2040
```

## Learning Goals

This project was created to practice:

* User input handling
* Conditional statements (if, elif, else)
* Date calculations
* Real-world problem solving with Python

## Author

## Author

Created by Mahendra.

Built while learning Python with guidance and debugging assistance from ChatGPT.

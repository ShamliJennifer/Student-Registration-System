# Student Registration & Contact Intelligence System

**Author:** S. Shamli Jennifer  
**GitHub:** [@ShamliJennifer](https://github.com/ShamliJennifer)  
**Course:** BCA Data Science

## About the Project

The Student Registration & Contact Intelligence System is a Python-based project used to manage student contact details.

It reads student information from a CSV file, checks whether the details are valid, identifies duplicate records and stores valid student records. It also provides options to register, search, update and delete student details.

## Technologies Used

- Python
- CSV file handling
- Python built-in modules

## Project Structure

```
Student-Registration-System/
├── proof/
│   └── test_cases.md
├── tests/
│   └── test_validator.py
├── analytics.py
├── contacts.csv
├── loader.py
├── main.py
├── README.md
├── students_clean.csv
├── validator.py
├── requirements.txt
├── .gitignore
└── CREDITS.md
```

## Features

1. Reads student contact details from a CSV file.
2. Validates student names, phone numbers and email addresses.
3. Detects duplicate phone numbers and email addresses.
4. Stores valid student records in a separate CSV file.
5. Displays all student records.
6. Searches students by name, phone number or email.
7. Registers new students.
8. Updates existing student details.
9. Deletes student records.
10. Generates an analytics report.

## Validation Rules

- Student name should not be empty.
- Phone number must contain exactly 10 digits.
- Phone number must start with 6, 7, 8 or 9.
- Email must contain exactly one @ symbol.
- Email must have a valid basic domain format.
- Duplicate phone numbers and email addresses are not allowed.

## How to Run the Project

### Step 1: Open the project folder

Open the `Student-Registration-System` folder in VS Code.

### Step 2: Run the main program

Open the terminal and enter:

```bash
python3 main.py
```

### Step 3: Select an option

The program displays a menu with the following options:

1. View Students
2. Search Student
3. Register Student
4. Update Student
5. Delete Student
6. Analytics Report
7. Save and Exit

Enter the option number to perform the required operation.

## Running the Tests

To run the validation tests, use:

```bash
python3 -m unittest discover -s tests -v
```

## CSV Files

- `contacts.csv` contains sample student contact details for testing.
- `students_clean.csv` stores the valid student records.

## Project Evidence

The `proof` folder contains documented test cases. Run the program and tests to create your own actual execution evidence if required for submission.

## Conclusion

This project demonstrates the use of Python functions, conditional statements, loops, CSV file handling, data validation, duplicate detection and basic data analysis.

## Credits

This is an independently written implementation inspired by the project idea in [the original DATA-SCINECE-PROJECT repository](https://github.com/vincentgit777-a11y/DATA-SCINECE-PROJECT). Please see [CREDITS.md](CREDITS.md) for the acknowledgement.

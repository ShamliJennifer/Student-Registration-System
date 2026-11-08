# Student Registration & Contact Intelligence System

**Author:** S. Shamli Jennifer  
**GitHub:** [@ShamliJennifer](https://github.com/ShamliJennifer)  
**Course:** BCA Data Science

A Python command-line application for managing student contact records. It imports CSV data, validates contact details, detects duplicates, and supports registering, viewing, searching, updating, deleting, and analysing student records.

> **Project note:** This is an independently written implementation based on the feature idea of the public project listed in [CREDITS.md](CREDITS.md). It does not claim authorship of that original project.

## Features
- Import student records from CSV.
- Validate names, Indian mobile-number format, and basic email format.
- Detect duplicate phone numbers and email addresses.
- View, search, register, update, and delete student records.
- Save records to `students_clean.csv`.
- Generate a data-quality and contact-distribution report.
- Run automated unit tests using Python's built-in `unittest`.

## Project structure
```
Student-Registration-System/
├── main.py
├── validator.py
├── loader.py
├── analytics.py
├── contacts.csv
├── students_clean.csv
├── tests/test_validator.py
├── proof/test_cases.md
├── requirements.txt
├── .gitignore
├── CREDITS.md
└── README.md
```

## Requirements
- Python 3.9 or newer
- No third-party packages required.

## Run the project
From the project folder, run:
```bash
python3 main.py
```
Follow the menu. The sample input is `contacts.csv`; current records are saved to `students_clean.csv` when you choose **Save and exit**.

## Run tests
```bash
python3 -m unittest discover -s tests -v
```

## Validation rules
- Name cannot be blank.
- Phone must contain exactly 10 digits and start with 6, 7, 8, or 9.
- Email must contain one `@`, no spaces, and a domain containing a dot.
- Duplicate phone numbers and email addresses are not accepted.

## Learning outcomes
Python functions, loops, conditional logic, exception handling, CSV file handling, sets, data validation, modular programming, and basic data analysis.

## Author
**S. Shamli Jennifer** · BCA Data Science  
[GitHub profile](https://github.com/ShamliJennifer)

See [CREDITS.md](CREDITS.md) for project inspiration and attribution.

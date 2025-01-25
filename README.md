# Strong Password Checker

A Python implementation of a password strength validator and generator that ensures secure password practices.

## Project Structure

```
strong-password-checker/
├── password_manager.py    # Core implementation of password checking and generation
├── tests.py              # Unit tests
├── .gitignore           # Git ignore file for Python (Don't worry about this)
└── README.md            # This file
```

## Project Goals

This project aims to:

1. Implement a robust password strength checker that validates passwords against security best practices
2. Provide a secure password generator that creates strong, random passwords

## Password Requirements

A strong password must meet the following criteria:

- Minimum length of 8 characters
- Maximum length of 100 characters
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one number
- Contains at least one special character

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/nitvob/strong-password-checker.git
cd strong-password-checker
```

2. Make sure you have Python 3.6+ installed on your system.

3. No additional dependencies are required as the project uses only Python standard library.

## Running Tests

To run the unit tests:

```bash
python -m unittest tests.py
```

The test suite includes:

- Validation of password requirements
- Testing password generation with various lengths
- Edge cases and error handling
- Uniqueness verification for generated passwords

## Functions

### `is_strong_password(password: str) -> bool`

Checks if a given password meets all the strength requirements.

### `generate_strong_password(length: int) -> str`

Generates a strong password of specified length that meets all requirements.

# 💱 Currency Converter

## 📌 Project Description
The Currency Converter is a simple Python-based project that converts one currency into another using predefined exchange rates.

It uses a Python dictionary to store exchange rates and functions to perform currency conversions.

## 🚀 Features
- Converts currencies between INR, USD, EUR, and GBP.
- Uses a dictionary to store exchange rates.
- Accepts decimal and whole-number amounts.
- Checks for negative amounts.
- Handles invalid numeric input using try-except.
- Validates currency codes entered by the user.
- Displays the converted amount up to 2 decimal places.

## 💻 Technologies Used
- Python
- Dictionary
- Functions
- Conditional Statements (if-else)
- Exception Handling (try-except)
- String Methods

## 💱 Supported Currencies

| Currency Code | Currency Name | Exchange Rate (INR) |
|---------------|---------------|--------------------|
| INR | Indian Rupee | 1 |
| USD | US Dollar | 83 |
| EUR | Euro | 90 |
| GBP | British Pound | 105 |

**Note:** These are predefined sample exchange rates and are not live market rates.

## ⚙️ How It Works
1. The program displays the available currencies.
2. The user enters the amount to be converted.
3. The program checks whether the amount is valid and non-negative.
4. The user selects the source currency and target currency.
5. The program validates both currency codes.
6. The source currency is first converted into INR.
7. INR is then converted into the target currency.
8. The final converted amount is displayed.

## ▶️ How to Run the Project

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run the following command:

```bash
python currency_converter.py
```

## 📤 Sample Output

```text
============CURRENCY CONVERTER============
Available Currencies are:
INR (Indian Rupees)
USD (United States Dollar)
EUR (Euro)
GBP (British Pound)

Enter amount: 100
Convert from following: INR, USD, EUR, GBP: USD
Convert to following: INR, USD, EUR, GBP: EUR

100.0 USD = 92.22 EUR
```

## 🎯 Learning Outcomes
Through this project, I learned:
- How to create and use dictionaries in Python.
- How to define and call functions.
- How to use conditional statements.
- How to handle invalid inputs using try-except.
- How to perform mathematical calculations.
- How to organize a Python project.

## 👩‍💻 Author
Created as a beginner-level Python project to practice programming concepts.

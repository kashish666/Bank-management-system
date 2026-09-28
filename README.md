# Bank Management System - Python OOPs & MySQL

A complete console-based Bank Management System built using Python (OOPs Concept) and MySQL for secure data handling.

This project demonstrates real-world banking operations with secure login and admin controls.

### Main Features - 3 Options

**1. Customer Registration**
   - New user can create bank account
   - Auto-generates Account Number

**2. Customer Login**
   - Secure Login with Account Number & PIN
   - Check Balance
   - Deposit Money
   - Withdraw Money
   - Money Transfer
   - View Transaction History

**3. Admin Login**
   - View All Customers
   - Search Customer by Account Number
   - Delete Customer Account
   - View All Transactions

### Tech Stack
- **Language:** Python
- **Database:** MySQL
- **Concepts Used:** OOPs, MySQL Connector, Exception Handling

### How to Run This Project (Setup)

**1. Database Setup**
- Open MySQL Workbench
- Import the `database.sql` file from this repository
- This will create `bank_management_system` database with all tables

**2. Python Setup**
- Install MySQL connector: `pip install mysql-connector-python`
- Open `BANKPROJ.PY` and update your MySQL password in connection:
  ```python
  mysql.connector.connect(host="localhost", user="root", password="YOUR_PASSWORD", database="bank_management_system")

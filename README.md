# Bank Management System - Python OOPs & MySQL

A complete console-based Bank Management System built using Python (OOPs Concept) and MySQL for secure data handling.

### Main Menu - 3 Options
1. Customer Registration
2. Customer Login
3. Admin Login

### 1. Customer Registration
- Stores: First Name, Last Name, DOB, City, State, Address, Phone, Pincode, Password
- After registration, a unique `Customer ID` is auto-generated and displayed.
- Customer can Login using Customer ID & Password.

### 2. Customer Login - Features

**a) My Profile**
   - View Profile: Displays all registration information
   - Update Profile: Update Email, Phone Number, Address

**b) My Account**
   - Create New Account
   - View Account Details

**c) Banking Operations**
   - Deposit Money
   - Withdrawal Money
   - Transfer Money
   - Account Statement

**d) Other Services**
   - Beneficiary Management
   - Loans: Apply for Loan, View Your Loan, Pay EMI, View EMI Statement

**e) Security**
   - Change Password
   - Logout

### 3. Admin Login
Admin logs in with Admin Password.

**Admin Features:**
- View All Customers
- View All Customer Accounts
- View Beneficiary of Customers
- View All Loans
- Approve / Reject Loan
- View All Loan Payments

### Tech Stack & Concepts Used
- **Language:** Python (OOPs - Class, Object, Inheritance)
- **Database:** MySQL
- **Data Handling:** CRUD operations, Data Validation, Transaction Management

### How to Run
1. Create database from `database.sql`
2. Install dependency: `pip install mysql-connector-python`
3. Run: `python main.py`

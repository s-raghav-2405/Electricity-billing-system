# ⚡ Electricity Billing System

A simple Python and MySQL based Electricity Billing System that allows administrators and customers to manage electricity billing records, verify customer details, view bills, and process bill payments.

---

## 📌 Project Overview

The Electricity Billing System is a console-based application developed using Python and MySQL. It provides basic functionalities for managing customer records and electricity bill payments.

### Features

* 👨‍💼 Admin/User Registration
* 👥 Customer Details Verification
* ✏️ Customer Information Update
* 💡 Electricity Bill Viewing
* 💳 Bill Payment Processing
* ✅ Payment Status Tracking

---

## 🛠️ Technologies Used

* Python
* MySQL
* MySQL Connector
* Datetime Module

---

## 📂 Database Tables

### Admin Table

| Column   | Type    |
| -------- | ------- |
| username | VARCHAR |
| admin_no | INT     |
| password | VARCHAR |

### Customer Table

| Column   | Type    |
| -------- | ------- |
| meter_no | INT     |
| name     | VARCHAR |
| address  | VARCHAR |
| phone    | BIGINT  |
| password | VARCHAR |

### Bill Table

| Column     | Type    |
| ---------- | ------- |
| bill_id    | INT     |
| meter_no   | INT     |
| units      | INT     |
| total_bill | DECIMAL |
| status     | VARCHAR |
| bill_date  | DATE    |

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/electricity-billing-system.git
cd electricity-billing-system
```

### Install Dependencies

```bash
pip install mysql-connector-python
```

### Create Database

```sql
CREATE DATABASE ebbooking;
```

### Configure Database Connection

Update the database credentials inside the Python file:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="your_password",
    database="ebbooking"
)
```

### Run the Application

```bash
python electricity_billing_system.py
```

---

## 📋 Application Menu

```text
-------- ELECTRICITY BILLING SYSTEM --------

1. User Login
2. Customer Details
3. Customer Payment
4. Exit
```

---

## 🔄 Workflow

### 1. User Login

* Register administrator details
* Store admin credentials in database
* Update or delete admin records

### 2. Customer Details

* Verify customer information
* View address and contact details
* Update customer records

### 3. Customer Payment

* View monthly bill
* Verify bill amount
* Pay electricity bill
* Update payment status

---

## 🎯 Learning Objectives

This project helps in understanding:

* Python Functions
* Loops and Conditions
* Exception Handling
* MySQL Database Connectivity
* CRUD Operations
* SQL Queries (INSERT, SELECT, UPDATE, DELETE)

---

## 🔮 Future Enhancements

* GUI using Tkinter
* Online Payment Gateway
* Email Notifications
* SMS Alerts
* Secure Login Authentication
* Monthly Bill Generation
* Admin Dashboard
* Customer Login System

---

## ⚠️ Limitations

* Console-based interface
* Plain text password storage
* Basic validation
* Limited error handling

---

## 📸 Sample Output

```text
-------- ELECTRICITY BILLING SYSTEM --------

---- way to check your bill -----

1. user_login
2. customer_details
3. customer_payment
4. exit
```

---

## 👨‍💻 Author

Raghav.S

* Python Developer
* Student Project

GitHub: https://github.com/s-raghav-2405

---

## ⭐ Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is developed for educational purposes and learning.

Feel free to use and modify it.

# Elliesam Daycare Management System

A desktop-based daycare management system built with **Python, Tkinter, and MongoDB** to help Elliesam Daycare manage children, staff, attendance, payments, daily activities, and other daycare records in one centralized application.

## Problem Statement

Elliesam Daycare needs an organized way to manage information about children, parents and guardians, staff, attendance, payments, and daily activities.

Managing these records manually can make it difficult to keep information organized, track payments and attendance, and quickly access important records.

## Solution

The **Elliesam Daycare Management System** provides a centralized desktop application where authorized users can manage daycare records efficiently.

The system provides different access levels for **administrators and caregivers**, allowing each user to access the functions relevant to their role.

## Features

* User authentication
* Role-based access for administrators and caregivers
* Child registration and management
* Parent/guardian information management
* Staff management
* Attendance tracking
* Daily activity records
* Payment recording
* Arrears tracking
* Admin dashboard with daycare statistics
* Pickup and drop-off records
* Reports and record management
* Edit and delete functionality for relevant records

## User Roles

### Administrator

The administrator can:

* View the admin dashboard
* Manage children's information
* Manage parents' and guardians' information
* Manage staff information
* View attendance records
* Edit and delete attendance records
* View payment records
* Monitor arrears
* View daily activities
* Manage daycare records
* View daycare statistics

### Caregiver

The caregiver can:

* View children under their care
* Record children's attendance
* Record payments
* View attendance history
* Record daily activities
* Record nap/rest times
* Add notes about each child's day
* Record children's drop-off and pick-up

## Admin Dashboard

The administrator dashboard provides an overview of the daycare's current records.

It displays:

* Number of registered children
* Number of registered staff
* Number of children present today
* Today's attendance summary
* Total payments received today

The dashboard retrieves information directly from **MongoDB** and displays updated statistics when the dashboard is opened.

## Attendance & Payments

The attendance section allows caregivers to record attendance and payment information for each child.

Each attendance record contains:

* Child
* Date
* Attendance status
* Expected fee
* Amount paid
* Arrears

Administrators can view attendance and payment history and manage existing records.

## Daily Activities

The activities section allows caregivers to record activities carried out during the day.

Activities can be stored and later viewed by administrators as part of the child's daycare records.

## Database

The application uses **MongoDB** to store daycare information.

The database contains collections for information such as:

* Children
* Staff
* Attendance
* Activities

MongoDB allows the application to store and retrieve daycare records efficiently.

## Technologies

* **Python** – Application logic
* **Tkinter** – Desktop graphical user interface
* **MongoDB** – Database
* **PyMongo** – MongoDB connection and database operations
* **Git & GitHub** – Source control

## Project Structure

```text
ellisam-daycare/
│
├── main.py
├── database.py
├── login.py
├── admin_dashboard.py
├── admin_attendance.py
├── admin_activities.py
├── children.py
├── staff.py
├── attendance.py
├── activities.py
├── requirements.txt
├── .gitignore
└── README.md
```


## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/elliesam-daycare.git
```

### 2. Navigate to the project directory

```bash
cd elliesam-daycare
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure MongoDB

Make sure MongoDB is available and configure the database connection in the application's database configuration.

### 7. Run the application

```bash
python main.py
```


## Future Improvements

* Parent portal
* Mobile application
* SMS notifications
* Online payment integration
* Automated notifications
* Advanced reporting and analytics
* Cloud deployment
* Parent communication features

## Author

**Idah Karwitha**

## License

This project is licensed under the **MIT License**.

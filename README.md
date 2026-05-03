# Network Asset & Incident Management System

A command-line tool built with Python and SQLite to help network 
administrators register network devices and track incidents 
against them in a structured, database-backed system.

---

## 💡 Why I Built This

During my CCNA coursework, I got curious about how network administrators 
actually keep track of dozens of devices and the issues that come up. 
At the same time, I had studied OOP and DBMS in my semester and wanted 
to apply them to something real. This project came from combining both — 
a simple but functional tool that models how real IT operations teams 
manage network infrastructure.

---

## ✨ Features

- Register network assets — routers, switches, servers
- Log incidents against specific devices with severity levels
- View all assets and incidents in a readable format
- Filter incidents by a specific asset
- Mark incidents as resolved
- Input validation to keep data consistent
- Duplicate IP address prevention at the database level

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Database:** SQLite (via Python's built-in sqlite3 module)
- **Design:** Object-Oriented Programming — Asset and Incident classes
- **Interface:** Command-Line (CLI)

---

## 📁 Project Structure

network_asset_manager/
├── main.py          # Entry point, CLI menu, user interaction
├── database.py      # All database operations (CRUD)
├── models/
│   ├── asset.py     # Asset class
│   └── incident.py  # Incident class
└── README.md

---

## ▶️ How to Run

Make sure you have Python 3 installed.

git clone https://github.com/YOURUSERNAME/network-asset-manager.git
cd network-asset-manager
python main.py

No external libraries needed — uses Python's built-in sqlite3 only.

---

## 🗄️ Database Schema

**Assets Table**
| Column     | Type    | Notes                    |
|------------|---------|--------------------------|
| id         | INTEGER | Primary Key, Auto        |
| name       | TEXT    | Device name              |
| type       | TEXT    | router / switch / server |
| ip_address | TEXT    | Unique                   |
| location   | TEXT    | Physical location        |
| status     | TEXT    | active / inactive        |

**Incidents Table**
| Column       | Type    | Notes                         |
|--------------|---------|-------------------------------|
| id           | INTEGER | Primary Key, Auto             |
| asset_id     | INTEGER | Foreign Key → Assets.id       |
| description  | TEXT    | What happened                 |
| severity     | TEXT    | low / medium / high           |
| date_reported| TEXT    | Auto-filled with today's date |
| resolved     | TEXT    | yes / no                      |

---

## 🔑 Key Concepts Applied

- **OOP** — Asset and Incident modeled as classes with encapsulation
- **Relational Database Design** — One-to-many relationship between Assets and Incidents
- **Foreign Key Constraint** — Ensures every incident links to a valid asset
- **JOIN Query** — Incidents display asset names instead of raw IDs
- **Input Validation** — Loops enforce correct values before database insertion
- **SQL Injection Prevention** — Parameterized queries throughout

---

## 🚧 Limitations & Honest Notes

This is a learning project built as a fresher. It runs locally via CLI 
and uses SQLite which is not meant for multi-user or large-scale use. 
Authentication and a web interface are intentional next steps — the current focus is on clean data modeling, relational database design, and OOP fundamentals.

---

## 👤 Author

[M Tanisha]  
[https://www.linkedin.com/in/tanisha-m-2a68b71b7/]  
[https://github.com/Tanishaaaa251]
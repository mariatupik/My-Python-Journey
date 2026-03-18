# MySQL Orders Manager

A Python-based database management tool designed to handle customer orders using MySQL. This project demonstrates how to perform automated data manipulation and retrieve relational information using complex SQL joins.

---

##  Key Features
* **Automated Order Processing:** Clears old data and populates the `orders` table based on specific user and category filters.
* **Relational Data Mapping:** Connects `users`, `items`, and `orders` using primary and foreign keys.
* **Advanced Reporting:** Uses `SQL JOIN` to generate a clear overview of which users ordered which items.
* **Data Integrity:** Implements `db.commit()` to ensure all transactions are safely saved.

---

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Database:** MySQL
* **Library:** `mysql-connector-python`

---

##  Database Structure
To use this script, ensure your MySQL database (`simple`) contains:
* **users**: `id`, `login`
* **items**: `id`, `title`, `category`
* **orders**: `user_id`, `item_id`

---

##  How to Run
1. Install the connector:
   ```bash
   pip install mysql-connector-python
   ```
2. Configure your credentials (`host`, `user`, `passwd`) in `mysql_orders_manager.py`.
3. Run the script:
   ```bash
   python mysql_orders_manager.py
   ```
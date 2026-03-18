import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="root",
    database="simple"
)
cursor = db.cursor()

cursor.execute("DELETE FROM orders")
cursor.execute("SELECT id FROM users WHERE login = 'john'")
user_id = cursor.fetchone()[0]
cursor.execute("SELECT id FROM items WHERE category = 'hats'")
items = cursor.fetchall()

for item in items:
    sql_insert = "INSERT INTO orders (user_id, item_id) VALUES (%s, %s)"
    val = (user_id, item[0])
    cursor.execute(sql_insert, val)
db.commit()
query = """
SELECT users.login, items.title 
FROM orders
JOIN users ON orders.user_id = users.id
JOIN items ON orders.item_id = items.id
"""
cursor.execute(query)
res = cursor.fetchall()

print("Всі замовлення\n")
for row in res:
    print(f"{row[0]}  –  {row[1]}")

cursor.close()
db.close()
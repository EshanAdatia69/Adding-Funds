# database.py
import sqlite3



def get_funds(username, password):
  conn = sqlite3.connect("database.db")
  cursor = conn.cursor()
  # Check if the data is present in the table
  cursor.execute('''
    SELECT username, password, funds FROM users
    WHERE username = ? AND password = ?
  ''', (username, password))

  # Fetch the results of the query
  results = cursor.fetchone()

  if results:
    # Data is present in the table
    return results[2]
  else:
    # Data is not present in the table
    return None

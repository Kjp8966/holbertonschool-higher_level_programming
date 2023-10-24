#!/usr/bin/python3
"""Module that lists all states from the hbtn_0e_0_usa database."""
import sys
import MySQLdb

if __name__ == "__main__":
        # Get MySQL credentials from command-line arguments
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
            cur = db.cursor()

                # Execute the SQL query to retrieve all states sorted by id
        cur.execute("""SELECT * FROM `states` WHERE name 
        LIKE BINARY 'N%'  ORDER BY states.id""")
        rows = cur.fetchall()
        for row in rows:
                print(row)
        cur.close()
        db.close()

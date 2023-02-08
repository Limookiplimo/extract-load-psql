import psycopg2 as db
from faker import Faker
import time

def write_read_data():
    fake=Faker()
    records = []
    i=1

    #loop through 1000 records to be written to db
    for r in range(1000):
        records.append((i, fake.name(), fake.street_address(), fake.city(), fake.zipcode()))
        i+=1
    #converT the array records to tupple
    to_db = tuple(records)

    #CONNECTION
    #establish db connection
    print("Establishing db connection")
    time.sleep(4)
    conn_string = "dbname='testdb' host='localhost' user='user' password='password'"
    conn = db.connect(conn_string)
    cur = conn.cursor()

    #DATA INSERTION
    #write data to db table called users(previously created)
    write_query = "insert into users(id, name, street, city, zip) values (%s,%s,%s,%s,%s)"
    #add query results to db
    cur.executemany(write_query, to_db)
    #commit transaction to make it permanent
    conn.commit()
    print("Inserting data into 'users' table")
    time.sleep(4)

    #DATA EXTRACTION
    #read data from users table
    print("Now reading data from the database")
    time.sleep(5)
    read_query = " select * from users"
    cur.execute(read_query)
    #check number of rows
    rows = cur.rowcount
    print(rows)
    #Get record of the first row
    data=cur.fetchone()
    print(data)


    #DATA SAVE
    #open file to write table to
    print("Saving extracted data into a CSV file")
    time.sleep(4)
    file = open('users.csv','w')
    #copy records to the file from users table separating each row with a comma
    cur.copy_to(file, 'users', sep=',')
    #close the file
    file.close()
    print("Done")

    #close connections
    cur.close()
    conn.close()

write_read_data()
import mysql.connector
from mysql.connector import Error
from category import *
connection = mysql.connector.connect(host='localhost',database='Pure_beure',user='root',password='')


cursor = connection.cursor()
cursor.execute("select database();")
record = cursor.fetchone()
print ("Your connected to - ", record)

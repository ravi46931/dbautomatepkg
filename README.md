# Project Description
## About
**dbconnector** is a Python package that provides flexible, interactive and expressive data manipulation with databases. It designed to make working with "relational" and "non-relational" databases seamless, interactive and efficient, provides a flexible and scalable solution for diverse data storage and retrievel needs.

## Table of Contents

- [Main Features](#main-features)
- [Where to get it](#where-to-get-it)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [How to use it](#how-to-use-it)
  - [Import the library for MySQL](#import-the-library-for-mysql)
  - [Create an instance of MySQL class](#create-an-instance-of-mysql-class)
  - [Connect to MySQL Server](#connect-to-mysql-server)
  - [Check the MySQL handler object](#check-the-mysql-handler-object)
  - [Execute query with MySQL](#execute-query-with-mysql)
  - [To insert the data in table](#to-insert-the-data-in-table)
  - [To save the data of the table](#to-save-the-data-of-the-table)
  - [To close the MySQL connection](#to-close-the-mysql-connection)
  - [Import the library for MongoDB](#import-the-library-for-mongodb)
  - [Create an instance of MongoDB class](#create-an-instance-of-mongodb-class)
  - [Get the client of MongoDB](#get-the-client-of-mongodb)
  - [Create database of MongoDB](#create-database-of-mongodb)
  - [Create collection of MongoDB](#create-database-of-mongodb)
  - [To insert the data in collection](#to-insert-the-data-in-collection)
  - [To find the data of the collection](#to-find-the-data-of-the-collection)
  - [To save the data of the collection](#to-save-the-data-of-the-collection)
  - [To delete the data of the collection](#to-delete-the-data-of-the-collection)
  - [To update the data of the collection](#to-update-the-data-of-the-collection)
  - [To close the mongo client](#to-close-the-mongo-client)
  - [Functionality](#functionality)
- [Development](#development)
  - [Important links](#important-links)
  - [Source code](#source-code)


## Main Features
Here are some of the key features of **dbconnector** as follows:<br>

- This **dbconnector** works with **MongoDB** as well as **MySQL** databases.
- When working with **MySQL**, it can executes any query, it can insert multiple type of data, it can save the data as well.
- When working with **MongoDB**, it creates *database* and *collection*, data can be insert, find, delete, and update as well, the data can be saved locally.

## Where to get it

The source code is currently hosted on **GitHub** at: 
https://github.com/ravi46931/dbconnectorpkg


## Installation

Install via pip:
```
# PyPI
pip install dbconnector
```

## Dependencies
**dbconnector** supports Python3.8, Python3.9, python3.11
Installation requires:
- pymongo
- pymongo[srv]
- dnspython
- pandas
- numpy
- termcolor
- mysql-connector-python
- prettytable

## How to use it

Let suppose you want to use **MySQL** database.

### Import the library for MySQL

```python
from dbautomate import mysqloperator
```

### Create an instance of MySQL class

```python
mysql_handler=mysqloperator.MySQL_connector()
```

### Connect to MySQL Server

```python
config = {
'host': 'your_mysql_host',
'user': 'your_mysql_user',
'password': 'your_mysql_password',
'database': 'your_database_name'
}
conn=mysql_handler.connect_to_mysql(config, attempts=3, delay=2)
# attempts: Number of times it tries to connect the server in case of failure.
# delay: time after which next attempt will happen
# These two parameters are optional
```
For successful connection it gives following message:<br>
<span style="color: lightgreen;"> Connected successfully....

### Check the MySQL handler object
```python
print(mysql_handler)
```
Output:<br>

MySQLHandler Object -<br>
Config: 
<span style="color: blue;">{'host': 'your_mysql_host', 'user': 'your_mysql_user', 'password': 'your_mysql_password', 'database': 'your_database_name'}</span><br>
Connected: <span style="color: blue;">True</span> <br>

### Execute query with MySQL

```python
query="select * from table_name"
mysql_handler.execute_query(query)
```
It prints table along with successful execution message.<br>
<span style="color: lightgreen;"> Query executed successfully....</span>

```
+----------------+------------+
| purchase_price | sale_price |
+----------------+------------+
| 8000           | 9505       |
+----------------+------------+
| 8500           | 10105      |
+----------------+------------+
| 7000           | 8505       |
+----------------+------------+
| 10500          | 11505      |
+----------------+------------+
```

### To insert the data in table

Insert single entry or multiple entries.
```python
table_name='cats'
values=[
('Mena',5),
('Kena',11)
]
mysql_handler.insert_data(table_name, values)
```
If you want to use different database to insert the data, you can achieve this by mentioning the database.
```python
db_name='book'
table_name='english_books'
values=[......]
mysql_handler.insert_data(table_name, values, db_name)
```

You can insert **CSV** file into the table as well.
```python
filepath='path/to/your/data.csv'
mysql_handler.bulk_insert(table_name, filepath)
# Change the database as well
filepath='path/to/your/data.csv'
db_name='books'
mysql_handler.bulk_insert(table_name, filepath, db_name)
```

1) If the first entry is *autoincrement* id, and you have not provided that in your input data (aka 'values' in above code) then enter 'y', but if you have provided in your input data then enter something else.<br>
2) If you are inserting the multiple entries then enter *y*.<br>
3) If you are inserting the single entry then enter *n*.<br>

A success message shows after successful insertion of the data.<br>
<span style="color: lightgreen;">Inserted successfully....</span>

### To save the data of the table
To save the *table* locally from the current active *database*.
```python
table_name='cats'
mysql_handler.save_data(table_name)
```
To save the data from the different *database*.
```python
db_name='animals'
table_name='cats'
mysql_handler.save_data(table_name, db_name)
```

Prints the success message after the saving data.<br>

Enter the filename: data.csv<br>
<span style="color: lightgreen;">File:</span> <span style="color: blue;">'data.csv'</span> <span style="color: lightgreen;">saved successfully....</span>

### To close the MySQL connection

```python
mysql_handler.close_connection()
```
It prints successful connection close.<br>
<span style="color: darkgrey;">MySQL connection closed.</span>

Let suppose you want to use **MongoDB** database.

### Import the library for MongoDB

```python
from dbautomate import mongodboperator
```

### Create an instance of MongoDB class
```python
mongo=mongodboperator.MongoDB_connector()
```

### Get the client of MongoDB
```python
uri="localhost:27017"
client=mongo.get_mongo_client(uri)
```
A success message prints.<br>
<span style="color: lightgreen;">Connected to MongoDB Successfully....</span>

### Create database of MongoDB
Ensure you have already created with client.
```python
database_name='firstdb'
mongo.create_database(database_name)
```
After creating database it prints success message.<br>
<span style="color: lightgreen;">Database created successfully....</span>


### Create collection of mongoDB
Ensure you have already created with client and database.
```python
collection_name='first'
mongo.create_collection(collection_name)
```
After creating collection it prints success message.<br>
<span style="color: lightgreen;">Collection created successfully....</span>

### To insert the data in collection

You can insert single or multiple entries.
```python
# Single Entry
single_entry={'name':'abc', 'age':24}
mongo.insert_data(single_entry)
```
A success message prints.<br>
<span style="color: lightgreen;">Inserted successfully(Single entry)....</span>


```python
# Multiple Entries
multiple_entries=[{'name':'abc', 'age':24},{'name':'def', 'age':22}]
mongo.insert_data(multiple_entries)
```
A success message prints.<br>
<span style="color: lightgreen;">Data inserted successfully....</span>


If you want to insert data from the **CSV**, **EXCEL** or **JSON** file, you can achieve this by following way.
```python
# To insert the data in the current collection
mongo.bulk_insert(filepath)
# To insert the data in a new or different collection
collection_name='employee'
mongo.bulk_insert(filepath, collection_name)
```
A success message prints.<br>
<span style="color: lightgreen;">Data inserted successfully....</span>

### To find the data of the collection

You can find the data.
```python
mongo.find_data()
```
1) If you want to see the data in the form of DataFrame enter *y*.
2) If you want to see the data in the form of List enter *n*.

### To save the data of the collection

You can save the data locally.
```python
mongo.save_data()
```
Enter the type of the file and name of the file (that you want to save).

Do you want to save the data as json file or csv file?(json/csv)json<br>
Enter the filename: q.json<br>
<span style="color: lightgreen;">File:</span> <span style="color: blue;">'q.json' </span> <span style="color: lightgreen;">saved successfully....</span>

### To delete the data of the collection

For deleting the entire data from the collection.

```python
mongo.delete_data()
```

Enter *y* if you want to delete the entire data.<br>
It will delete entire data, Do you want to delete the data?(y/n): *y*<br>
<span style="color: magenta;">All entry deleted</span>

For delete the data based on the key value.

```python
key_value={'age':25}
mongo.delete_data(key_value)
```

Enter *one* if you want to delete the one entry else *many* it delete all the entry based on the *key_value*
Do you want delete the one entry or mutiple entries?(one/many) one

Option: *one*<br>
<span style="color: lightgreen;">Entry deleted successfully</span>

Option: *many*<br>
<span style="color: lightgreen;">Multiple entries deleted successfully</span>

### To update the data of the collection

```python
filter_criteria={'age': 25}
update_data=[{'$set': {'age':24}}]
mongo.update_data_entry(filter_criteria, update_data)
```

Enter *one* if you want to update the single entry.

Do you want single entry update on multiple?(one/many) one<br>
<span style="color: lightgreen;">Updated Successfully (one entry)... </span>

Enter *many* if you want to update the multiple entries.

Do you want single entry update on multiple?(one/many) many<br>
<span style="color: lightgreen;">Updated Successfully (multiple entries)....</span>

### To close the mongo client

```python
mongo.close_mongo_client()
```

After successful closing the client.<br>
<span style="color: magenta;">MongoDB client closed successfully..</span>

### Functionality

For more detail of each of the functions can be reed the docstrings

```python
print(mysql_handler.insert_data.__doc__)
```

## Development

### Important links

- Source code repo: [GitHub Link](https://github.com/ravi46931/dbconnectorpkg)
- Download Release: [Pypi](https://pypi.org/project/dbautomate/)
- Bugs/ Feature requests: [GitHub issue Tracker](https://github.com/ravi46931/dbconnectorpkg/issues)

### Source code

You can check the latest sources with the command:

```
https://github.com/ravi46931/dbconnectorpkg.git
```

[Go to top](#table-of-contents)
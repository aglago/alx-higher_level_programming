# Learning Objectives
Below are the questions you should be able to answer after completing the SQL project.

This file explains and answers these questions in case you have any unlearned gaps.

## General

- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries
- How to use MySQL functions

## Answers

### What's a database ?
In simple terms, a database is a collection of data that is organized and stored in a computer system. It can contain different types of information, like text, numbers, images, and videos.

A database is often used to store information for applications like websites or mobile apps. It's a fundamental part of any software system, and learning how to work with databases is an essential skill for any software engineer.

### What's a relational database ?
A relational database is a specific type of database that organizes data into tables. Each table contains rows and columns of data, and the tables are related to each other through the use of keys. 

The main advantage of a relational database is that it allows for a high level of flexibility and scalability. For example, if you want to add new information to the database, you can simply add a new row to an existing table. You don't need to change the structure of the entire database.

### What does SQL stand for ?
SQL stands for "Structured Query Language". As the name suggests, SQL is a language that is used to query or interact with a database. It allows you to create, read, update, and delete data in a database. It's also sometimes called "sequel", as a pun on the word "sequential".

SQL is a declarative language, which means that you tell the database what you want to do, instead of how to do it.

### What is MySQL ?
MySQL is a popular open-source relational database management system (RDBMS) that is written in C and C++. It's based on the SQL language and is widely used in web applications and other software systems. 

MySQL is free to use and is licensed under the GNU General Public License. It's often used in combination with the PHP programming language to create dynamic websites.

### How to create a database in MySQL ?
Create a database in MySQL using the command-line interface (CLI). First, you need to open the CLI and connect to the MySQL server. You can do this by running the "mysql" command. 

```sql
sudo mysql
```

Once you're connected, you can use the "CREATE DATABASE" statement to create a new database. For example, you can run the following command:

```sql
mysql> CREATE DATABASE mydb;
```

### What does DDL and DML stand for ?
DDL stands for "Data Definition Language" and DML stands for "Data Manipulation Language". DDL is a type of SQL query that is used to create, alter, and drop tables and other database objects. DML, on the other hand, is used to insert, update, and delete data from a database. So DDL is used to define the structure of the database, while DML is used to manipulate the data within it.

You can use the 'USE' command to switch to a particular database. Forexample

```sql
USE mydb;
```

will take you into the `mydb` database to be used.


### How to CREATE a table ?

Now that you're in the right database, you can start adding tables. To add a table, you can use the "CREATE TABLE" command. This command takes a few arguments, including the name of the table, the columns in the table, and the data type for each column. You can also add constraints and other properties to the table. Let's take an example:

Let's say you want to create a table called "products" that contains information about products sold by a company. You can create this table by running the following command:

```sql
CREATE TABLE products (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    CONSTRAINT products_pk PRIMARY KEY (id)
);
```

I know that's a lot of information to take in, so let's break it down. 

The first argument, "CREATE TABLE", is the command that tells MySQL to create a new table. 

The next argument, "products", is the name of the table. 

The next few arguments define the columns in the table, and they include the name of the column, the data type, and whether or not the column is required. 

The last argument, "CONSTRAINT", is used to add a constraint to the table. 

After creating the table, you might want to view the table, you can use the `DESCIRBE` command to do that.

```sql
DESCRIBE products;
```

### How to ALTER a table ?

To alter a table, you can use the "ALTER TABLE" command. The "ALTER TABLE" command allows you to add, modify, and remove columns from a table. You can also use it to add and remove indexes and constraints. So to alter the "products" table, you would use the following command:

```sql
ALTER TABLE products ADD COLUMN quantity INT NOT NULL;
```

That will add a new "quantity" column to the "products" table, which will be an integer and can't be empty.

To remove a column, you use the "DROP COLUMN" clause in the "ALTER TABLE" command. So to remove the "quantity" column that we just added, you would use the following command:

```sql
ALTER TABLE products DROP COLUMN quantity;
```

That will delete the "quantity" column from the "products" table. You can also use the "ALTER TABLE" command to add and remove indexes and constraints.

**All the things ALTER TABLE can do for you**
In addition to adding and dropping columns, you can also use the "ALTER TABLE" command to:
1. Change the data type of a column.
2. Change the name of a column.
3. Change the default value of a column.
4. Change the nullability of a column.
5. Add or drop a primary key or a foreign key.
6. Add or drop an index.
7. Add or drop a check constraint.
So you have a lot of options for modifying tables with the "ALTER TABLE" command.

### How to SELECT data from a table
To select data from a table, you would use the "SELECT" statement in SQL. The basic format of the "SELECT" statement is as follows:

```sql
SELECT column1, column2, ..., columnN
FROM table_name
WHERE condition;
```

So, for example, to select the "name" and "age" columns from the "people" table, you could use the following query:

```sql
SELECT name, age
FROM people;
```

This query would return all the rows from the "people" table that have values in the "name" and "age" columns.

### How to INSERT data

To insert data into a table, you can use the "INSERT" command. The "INSERT" command takes two main arguments: the name of the table to insert into, and a list of values to insert. So, for example, to insert a record into the "products" table, you would use the following command:

```sql
INSERT INTO products (name, description, quantity) VALUES ("Bag of Chips", "Delicious chips!", 100);
```

That will insert a row into the "products" table with the given values. You can use the "SELECT" command to retrieve the data from the table.

If you want to add multiple rows at once, you can use the "VALUES" keyword to specify a list of values to insert. For example, to insert three rows into the "products" table, you could use the following command:

```sql
INSERT INTO products (name, description, quantity) VALUES 
("Bag of Chips", "Delicious chips!", 100),
("Pizza", "Tasty pizza!", 200),
("Chocolate", "The best chocolate!", 300);
```

This will insert three rows into the "products" table, with the given values. You can use this technique to insert any number of records you want into a table.

You can use single quotes instead of double quotes in the "INSERT" command. So, for example, the above command could also be written like this:

```sql
INSERT INTO products (name, description, quantity) VALUES (‘Bag of Chips’, 'Delicious chips!', 100),
(‘Pizza’, 'Tasty pizza!', 200),
(‘Chocolate’, 'The best chocolate!', 300);
```

The single quotes and double quotes are interchangeable in this context. You just need to be consistent with your choice of quotes throughout the command.

### How to UPDATE data
The "UPDATE" command allows you to change the values of existing records in a table. For example, to change the price of the "shirts" product to $25, you could use the following command:

```sql
UPDATE products SET price = 25 WHERE name = 'shirts';
```

This command updates the "price" column for the record with the "name" value of "shirts" to 25. You can also update multiple records at once by using a "WHERE" clause that matches multiple records.

### How to DELETE data

The "DELETE" command allows you to delete records from a table. For example, to delete the record with the "name" value of "shirts", you could use the following command:

```sql
DELETE FROM products WHERE name = 'shirts';
```

This command will delete the record with the "name" value of "shirts" from the "products" table. You can also use a "WHERE" clause to delete multiple records at once.

### What are subqueries

A subquery is a query that is nested inside another query. Subqueries are useful for filtering or joining data from multiple tables. For example, let's say you want to find all the records in the "products" table with a "price" value less than the average "price" in the "products" table. You could use the following command:

```sql
SELECT * FROM products
WHERE price < (SELECT AVG(price) FROM products);
```

This command uses a subquery to find the average "price" in the "products" table, and then uses that value to filter the records.

### How to use MySQL functions

MySQL has a very wide range of functions, but here are some of the most commonly used ones:
- COUNT(): Counts the number of records that match a given condition.
- AVG(): Calculates the average value of a column.
- MIN(): Finds the smallest value in a column.
- MAX(): Finds the largest value in a column.
- SUM(): Calculates the sum of the values in a column.
- SUBSTR(): Extracts a substring from a string.
- CONCAT(): Concatenates two or more strings together.
- IFNULL(): Returns a default
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



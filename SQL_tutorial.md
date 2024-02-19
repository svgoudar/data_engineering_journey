# SQL (Structural Query Language)

Read [SQL](https://www.geeksforgeeks.org/sql-tutorial/?ref=lbp) for an overview. The following sections will go into more details.

### SQL is case insensitive

##  Attribute:
Attributes are the properties that define a relation. e.g.; ROLL_NO, NAME etc.
## Tuple:
Each row in the relation is known as tuple. The above relation contains 4 tuples, one of which is shown as:

 1	RAM	DELHI	9455123451	18
## Degree:
The number of attributes in the relation is known as degree of the relation. The STUDENT relation defined above has degree 5.
## Cardinality:
The number of tuples in a relation is known as cardinality. The STUDENT relation defined above has cardinality 4.


### Create Table


`CREATE TABLE Customer(
     CustomerID INT PRIMARY KEY,
     CustomerName VARCHAR(50),
     LastName VARCHAR(50),
     Country VARCHAR(50),
     Age INT ,
   	Phone INT
 );`

## Describe the columns of the table.
`SELECT COLUMN_NAME  
FROM information_schema.COLUMNS  
WHERE TABLE_NAME = 'customer';`

` SELECT ordinal_position , table_name , column_name , data_type , is_nullable FROM information_schema.columns where table_name = 'customer';`

`select * from customer;`

## Import from CSV file into DB

`COPY customer from 'C:\POSTGRES\organizations-100.csv' DELIMITER ',' CSV HEADER;`



## DATA TYPES

    CREATE TABLE data_types_example (
    -- Numeric Types
    column_integer INTEGER,
    column_bigint BIGINT,
    column_smallint SMALLINT,
    column_decimal DECIMAL(10, 2),
    column_real REAL,
    column_double DOUBLE PRECISION,

    -- Character Types
    column_char CHAR(50), (Fixed-Length non-Unicode Characters)
    column_varchar VARCHAR(100) (Variable-Length non-Unicode Characters),
    column_text TEXT ( Variable Length maximum length of 2,127,483,647 charactersnon-Unicode data),

    -- Binary Types
    column_bytea BYTEA,

    -- Date/Time Types
    column_date DATE,
    column_time TIME,
    column_timestamp TIMESTAMP,
    column_timestamp_tz TIMESTAMP WITH TIME ZONE,
    column_interval INTERVAL,

    -- Boolean Type
    column_boolean BOOLEAN,

    -- Geometric Types
    column_point POINT,
    column_polygon POLYGON,

    -- Network Address Types
    column_inet INET,
    column_cidr CIDR,

    -- JSON Types
    column_json JSON,
    column_jsonb JSONB,

    -- Arrays
    column_integer_array INTEGER[],

    -- Enumerated Types
    column_mood mood,

    -- UUID Type
    column_uuid UUID,

    -- Custom Types
    column_custom_color color);


## DDL, DML, TCL and DCL

https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/

### DDL (Data Definition Language)
  Data Definition Language is used to define the database structure or schema. DDL is also used to specify additional properties of the data. 
  
  #### CREATE
    
    
This command is used to create the database or its objects (like table, index, function, views, store procedure, and triggers).

  `CREATE TABLE Customer(
     CustomerID INT PRIMARY KEY,
     CustomerName VARCHAR(50),
     LastName VARCHAR(50),
     Country VARCHAR(50),
     Age INT ,
   	Phone INT
 )`

 `create table cutomer_tab as select * from customer where customername LIKE 'A%';`

 #### DROP
 This command is used to delete objects from the database.


`DROP TABLE table_name;`

#### ALTER TABLE – ADD, DROP, MODIFY

`ALTER TABLE table_name ADD (Columnname_1  datatype,Columnname_2  datatype, Columnname_n  datatype);`

`ALTER TABLE table_name
DROP COLUMN column_name;`

`ALTER TABLE table_name
MODIFY column_name column_type;`

`ALTER TABLE Student ADD 
 (AGE number(3),COURSE varchar(40));`

#### TRUNCATE

The major difference between TRUNCATE and DROP is that truncate is used to delete the data inside the table not the whole table.

`TRUNCATE TABLE  table_name;`

#### COMMENTS

   * Single Line Comments
        
        -- Commented sql
   * Multi Line comments
      
      /* dfdff
      
      fdffd */

   * Inline Comments

        SELECT customer_name, 
/* This column contains the name of 
the customer / order_date / 
This column contains the date the
order was placed */ FROM orders;

#### RENAME

`ALTER TABLE table_name
RENAME COLUMN old_name TO new_name;`




### DQL (Data Query Language)

* #### SELECT
    `SELECT * FROM table_name;`
    
    `SELECT CustomerName FROM Customer where Age = '21'; `

### DML (Data Manipulation  Language)

The SQL commands that deal with the manipulation of data present in the database belong to DML or Data Manipulation Language and this includes most of the SQL statements. 

* #### INSERT

    `INSERT INTO table_name (column1, column2, column3) VALUES ( value1, value2, value3);`

    `INSERT INTO Student VALUES 
('5','HARSH','WEST BENGAL',
'XXXXXXXXXX','19');`

    `INSERT INTO Student (ROLL_NO, 
NAME, Age) VALUES ('5','PRATIK','19');`

    `INSERT INTO first_table(names_of_columns1) 
SELECT names_of_columns2 FROM second_table; `

    `INSERT INTO table1 SELECT * FROM table2 WHERE condition;`

    `INSERT INTO Student 
SELECT * FROM LateralStudent;`

    `INSERT INTO Student SELECT * 
FROM LateralStudent WHERE Age = 18;`

    `INSERT INTO STUDENT(ID, NAME,AGE,GRADE,CITY) 
VALUES(1,"AMIT KUMAR",15,10,"DELHI"),
(2,"GAURI RAO",18,12,"BANGALORE"),
(3,"MANAV BHATT",17,11,"NEW DELHI"),
(4,"RIYA KAPOOR",10,5,"UDAIPUR");`

    
* #### UPDATE
    `UPDATE Customer SET CustomerName  
= 'Nitin' WHERE Age = 22;`

    `UPDATE Customer SET CustomerName = 'Shubham';`

* #### DELETE 
    `DELETE FROM GFG_Employees WHERE NAME = 'Rithvik';`
    
    `DELETE FROM GFG_Employees 
WHERE department = 'Development';`
    
    `DELETE FROM GFG_EMPLOyees;`

## DCL (Data Control Language)

DCL includes commands such as GRANT and REVOKE which mainly deal with the rights, permissions, and other controls of the database system. 

`GRANT SELECT, INSERT, DELETE, UPDATE ON Users TO 'Amit'@'localhost';`

`GRANT ALL ON Users TO 'Amit'@'localhost';`

`GRANT SELECT  ON Users TO '*'@'localhost';`

`GRANT EXECUTE ON FUNCTION Calculatesalary TO 'Amit'@'localhost';`

`revoke insert, 
select on accounts from Ram`

`revoke privilege_name on object_name
from {user_name | public | role_name}`

## TCL (Transaction Control Language)
Transactions group a set of tasks into a single execution unit. Each transaction begins with a specific task and ends when all the tasks in the group are successfully completed.
* ### TRANSACTION
    `BEGIN TRANSACTION transaction_name ;`

    `SET TRANSACTION [ READ WRITE | READ ONLY ];`
    
    `COMMIT;`

    `START TRANSACTION;`

    `UPDATE table_name SET column1 = new_value WHERE condition;`

    `DELETE FROM another_table WHERE another_condition;`

    `COMMIT;`


* ### ROLLBACK Command
    `START TRANSACTION;`

    `UPDATE table_name SET column1 = new_value WHERE condition;`

    Something unexpected happens, so rollback the changes
    `ROLLBACK;`

    or using a SAVEPOINT

    `SAVEPOINT my_savepoint;`

    `UPDATE table_name SET column2 = new_value WHERE condition;`

    Something else goes wrong, rollback to the savepoint
    
    `ROLLBACK TO my_savepoint;`

    `COMMIT;`

* ### SAVEPOINT

    `START TRANSACTION;`

    `INSERT INTO table_name (column1, column2) VALUES (value1, value2);`

    `SAVEPOINT my_savepoint;`

    `UPDATE table_name SET column1 = new_value WHERE condition;`

    If something goes wrong, rollback to the savepoint
    
    `ROLLBACK TO my_savepoint;`

    `COMMIT;`

## SQL VIEWS

`create view customer_view as select customername,country from customer where customername not LIKE 'S%'; `

`select * from customer_view where customername LIKE 'S%';`

`SELECT * FROM information_schema.VIEWS where view_definition like '%customer%'; `

Insert is not allowed

`insert into customer_view values ('sanjuuu','kl');`

But in this case

`create or replace view customer_view_1 as select * from customer;`

insert is allowed

`insert into customer_view_1 values (100,'sanjuuu','kl','INDIA',43,234567);`










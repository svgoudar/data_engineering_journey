- ### Performance Tuning

  - Major factors that will influence how many computations you must perform and how long it takes for your query to run:

    - **Table size**: Performance may be impacted if your query hits one or more tables with millions of rows or more.
    - **Joins**: Your query is likely to be slow if it joins two tables in a way that significantly raises the number of rows in the return set.
    - **Aggregations**: Adding several rows together to create a single result needs more processing than just retrieving those values individually.
    - **Other users executing queries**: The more queries a database has open at once, the more it must process at once, and the slower it will all be. It can be particularly problematic if other users are using a lot of resources to perform queries that meet some of the aforementioned requirements.

- ### Optimizing a Query for SQL:
  - SELECT fields instead of using SELECT *:
  - Avoid SELECT DISTINCT:
  - Create  queries with INNER JOIN (not WHERE or cross join):
  - Use WHERE instead of HAVING to define filters:
  - Use wildcards at the end of a phrase only
  - Use LIMIT to sample query results:
  - Run your query during off-peak hours

- ### EXPLAIN
 
  - In SQL, the EXPLAIN keyword provides a description of how the SQL queries are executed by the databases.
  - The DESCRIBE and EXPLAIN statements are synonyms. In practice, the DESCRIBE keyword is more often used to obtain information about table structure, whereas EXPLAIN is used to obtain a query execution plan (that is, an explanation of how MySQL would execute a query).  

```sql

SET @@explain_format=TRADITIONAL;
SET @@explain_format=json;
SET @@explain_format=tree;
EXPLAIN select movie_name from movie where  movie_name like 'S%'; 	
select @@explain_format;

```

- ### Stored Procedure
  
  - Stored Procedures are created to perform one or more DML operations on Database. It is nothing but the group of SQL statements that accepts some input in the form of parameters and performs some task and may or may not return a value.
  ```sql
  USE `learn_sql`;
  DROP procedure IF EXISTS `new_procedure`;

  DELIMITER $$  
  USE `learn_sql`$$
  CREATE PROCEDURE `new_procedure` (`movie` varchar(20))
  BEGIN
  select  * from movie where movie_name=@movie;
  END$$

  DELIMITER ;
  
  
  -----------------------------
  
  CREATE DEFINER=`root`@`localhost` PROCEDURE `new_procedure`(inout movie_n text)
  BEGIN
  set movie_n = (select  genre from movie where movie_name = movie_n);
  END
  
  
  set @mv='The Godfather';
  call new_procedure(@mv);
  select @mv;
  
  
  set @movie = 'The Godfather';
  prepare sd from 'call new_procedure( ? ) ';
  execute sd using @movie;
  select @movie;

  select * from information_schema.routines where LOWER(ROUTINE_TYPE)="procedure";

  ```


- ### SQL TRANSACTION
  - Properties of Transaction
    - Atomicity: The outcome of a transaction can either be completely successful or completely unsuccessful. The whole transaction must be rolled back if one part of it fails.
    - Consistency: Transactions maintain integrity restrictions by moving the database from one valid state to another.
    - Isolation: Concurrent transactions are isolated from one another, assuring the accuracy of the data.
    - Durability: Once a transaction is committed, its modifications remain in effect even in the event of a system failure.

- ### auto increment in sql

```sql
select @@auto_increment_increment;
SET @@auto_increment_increment=new_interval_value;
```

- ### PARTITION AND WINDOW FUNCTIONS

  - A PARTITION BY clause is used to partition rows of table into groups. It is useful when we have to perform a calculation on individual rows of a group using other rows of that group.
  ```sql
  select avg(rating) over (partition by genre) as avg_rat, movie_name, genre, rating from movie order by avg_rat desc; 
  ```
  
  ```sql
  
  select row_number() over (order by ExperienceInCurrentDomain) as row_num , Education, ExperienceInCurrentDomain, rank() over (order by Gender) as rank_n, dense_rank() over (partition by City) as dense_rnk,Age,City,Gender  from employee;

  ```
  - WINDOW Function
    - RANK()  
        As the name suggests, the rank function assigns rank to all the rows within every partition. Rank is assigned such that rank 1 given to the first row and rows having same value are assigned same rank. For the next rank after two same rank values, one rank value will be skipped. 
 
    - DENSE_RANK()  
        It assigns rank to each row within partition. Just like rank function first row is assigned rank 1 and rows having same value have same rank. The difference between RANK() and DENSE_RANK() is that in DENSE_RANK(), for the next rank after two same rank, consecutive integer is used, no rank is skipped. 

    - ROW_NUMBER() – 
        It assigns consecutive integers to all the rows within partition. Within a partition, no two rows can have same row number. 

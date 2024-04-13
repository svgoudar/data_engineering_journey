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



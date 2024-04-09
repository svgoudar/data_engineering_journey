- ## JOINS
- SQL Join statement is used to combine data or rows from two or more tables based on a common field between them. Different types of Joins are as follows: 

  - INNER JOIN
  - LEFT JOIN
  - RIGHT JOIN
  - FULL JOIN
  - NATURAL JOIN 

  
  - ### INNER JOIN
    - The INNER JOIN keyword selects all rows from both the tables as long as the condition is satisfied. This keyword will create the result-set by combining all rows from both the tables where the condition satisfies i.e value of the common field will be the same.
    
    ```sql
    select movie.movie_name, movie.release_year, movie_copy.movie_name, movie_copy.release_year from movie inner join movie_copy on movie.movie_name = movie_copy.movie_name;
    select movie.movie_name, movie.release_year, movie_copy.movie_name, movie_copy.release_year from movie join movie_copy on movie.movie_name = movie_copy.movie_name; -- JOIN is als same as INNER JOIN
    ```
    
  
  - ### LEFT JOIN
    - This join returns all the rows of the table on the left side of the join and matches rows for the table on the right side of the join. For the rows for which there is no matching row on the right side, the result-set will contain null. LEFT JOIN is also known as LEFT OUTER JOIN.
    
    ```sql
    select  movie.movie_name, movie.release_year, movie_copy.movie_name, movie_copy.release_year from movie left join movie_copy on movie.movie_name = movie_copy.movie_name;
    ```
  - ### RIGHT JOIN
    - RIGHT JOIN is similar to LEFT JOIN. This join returns all the rows of the table on the right side of the join and matching rows for the table on the left side of the join. For the rows for which there is no matching row on the left side, the result-set will contain null. RIGHT JOIN is also known as RIGHT OUTER JOIN.
    ```sql
    select  movie.movie_name, movie.release_year, movie_copy.movie_name, movie_copy.release_year from movie right join movie_copy on movie.movie_name = movie_copy.movie_name;
    ```
  - ### FULL OUTER JOIN
  ```sql
    select  mv_1.movie_name, mv_1.release_year, mv_2.movie_name, mv_2.release_year from movie as mv_1 left join movie_copy as mv_2 on mv_1.movie_name = mv_2.movie_name
    union
    select  movie.movie_name, movie.release_year, movie_copy.movie_name, movie_copy.release_year from movie right join movie_copy on movie.movie_name = movie_copy.movie_name;
  ```

 - ### CROSS JOIN
  - Cross Join is also called a Cartesian Join as it performs cross product of records of two or more joined tables. 
  ```sql
  select * from movie cross join movie_copy; 
  ```

 - ### SELF JOIN
 ```sql
    select  mv_1.movie_name, mv_1.release_year, mv_2.movie_name, mv_2.release_year from movie mv_1 join movie_copy mv_2 on mv_1.movie_name = mv_2.movie_name;
 ```
 - ### UPDATE JOIN
 - SQL UPDATE JOIN could be used to update one table using another table and join condition.


 ```sql
 update movie join movie_copy on movie.release_year = movie_copy.release_year set movie.movie_name = movie_copy.movie_name;
 ```
- ### Delete Join
- DELETE JOIN allows to delete rows from a table based on condition involving another table.
  ```sql
    DELETE library_books
    FROM  library_books JOIN students ON
    students.student_id =library_books.lib_id
    WHERE lib_id= 1001
  ```
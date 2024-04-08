
![img.png](clauses.png)

```sql
select * from movie where release_year > 2000;
select * from movie where release_year >= 1972;
select * from movie where release_year < 1972;
select * from movie where release_year <= 1972;
select * from movie where release_year = 1972;
select * from movie where release_year <> 2000;
select * from movie where release_year between 1972 and 1995;
select * from movie where movie_name not like 'S%';
select * from movie where movie_name not like '% %';
select * from movie where movie_name like '% %';
select * from movie where movie_name like 'S%';
select * from movie where release_year in (1971,2000);
```